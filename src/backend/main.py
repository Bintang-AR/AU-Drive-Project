from fastapi import FastAPI, UploadFile, File, Form
from fastapi.middleware.cors import CORSMiddleware
from datetime import datetime
from audio.convert import webm_to_wav
from services.inference import run_inference
from utils.vibration import generate_vibration_data

app = FastAPI(title="Machine Diagnostics API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/api/health")
async def health_check():
    return {
        "status": "ok",
        "timestamp": datetime.now().isoformat()
    }

# ===============================
# KELAS (sesuai label_map.joblib)
# ===============================
NORMAL_CLASSES = {"normal_engine_idle", "normal_brakes"}
NOT_ENGINE_CLASS = "not an engine"

# Rata-rata probabilitas minimum agar hasil dianggap valid.
# Nilai awal, sesuaikan setelah diuji dengan rekaman nyata.
VALID_CONFIDENCE_THRESHOLD = 0.50

# ===============================
# ISSUE MAPPING
# ===============================
ISSUE_MAP = {
    "bad_ignition": {
        "severity": "medium",
        "component": "Sistem Pengapian",
        "description": "Suara mengindikasikan sistem pengapian tidak optimal",
        "recommendation": "Periksa busi, koil, dan kabel pengapian"
    },
    "dead_battery": {
        "severity": "medium",
        "component": "Aki / Sistem Kelistrikan",
        "description": "Suara mengindikasikan aki lemah atau tekor",
        "recommendation": "Cek tegangan aki dan kondisi alternator, ganti aki bila perlu"
    },
    "low_oil": {
        "severity": "medium",
        "component": "Pelumasan",
        "description": "Indikasi oli rendah atau sudah aus",
        "recommendation": "Cek level oli dan tambah atau ganti oli mesin"
    },
    "power_steering": {
        "severity": "medium",
        "component": "Power Steering",
        "description": "Terdeteksi suara abnormal pada sistem power steering",
        "recommendation": "Periksa level dan kondisi minyak power steering serta selangnya"
    },
    "serpentine_belt": {
        "severity": "medium",
        "component": "Belt Serpentine",
        "description": "Terdeteksi suara abnormal pada belt serpentine",
        "recommendation": "Periksa ketegangan dan keausan belt, ganti bila retak atau aus"
    },
    "worn_out_brakes": {
        "severity": "high",
        "component": "Sistem Rem",
        "description": "Terdeteksi suara yang mengindikasikan kampas rem aus",
        "recommendation": "Segera periksa dan ganti kampas rem demi keselamatan"
    },
}

@app.post("/api/analyze")
async def analyze_audio(
    file: UploadFile = File(...),
    mode: str = Form(...)
):
    audio_bytes = await file.read()

    # ===============================
    # SAFE INFERENCE
    # ===============================
    wav_bytes = None
    try:
        wav_bytes = webm_to_wav(audio_bytes)
        label, confidence, probabilities = run_inference(wav_bytes)
    except Exception as e:
        print("❌ Inference error:", e)
        label = "unknown"
        confidence = 0.0
        probabilities = {}

    # ===============================
    # VALIDATION
    # ===============================
    issues = []

    if label == "unknown" or confidence < VALID_CONFIDENCE_THRESHOLD:
        # Hasil tidak meyakinkan: jangan dipaksa jadi "normal"
        label = "uncertain"
        issues.append({
            "id": "uncertain",
            "severity": "low",
            "component": "Hasil Analisis",
            "description": "Hasil analisis kurang meyakinkan",
            "recommendation": "Ulangi rekaman di area lebih tenang dengan mikrofon lebih dekat ke mesin"
        })
    elif label == NOT_ENGINE_CLASS:
        issues.append({
            "id": "not_an_engine",
            "severity": "low",
            "component": "Rekaman Audio",
            "description": "Suara yang direkam tidak terdeteksi sebagai suara mesin",
            "recommendation": "Dekatkan mikrofon ke mesin yang sedang menyala lalu ulangi rekaman"
        })
    elif label in ISSUE_MAP:
        issue = ISSUE_MAP[label].copy()
        issue["id"] = label
        issues.append(issue)
    # label di NORMAL_CLASSES: tidak ada issue

    # ===============================
    # HEALTH LOGIC
    # ===============================
    if label in NORMAL_CLASSES:
        overall_health = int(90 + confidence * 10)            # 90-100
    elif label in ISSUE_MAP:
        overall_health = max(30, int((1 - confidence) * 100))
    else:
        # uncertain / not an engine: skor kesehatan tidak bisa dihitung
        overall_health = None

        try:
            vibration_data = (
                generate_vibration_data(wav_bytes, 100 if mode == "quick" else 300)
                if wav_bytes else []
            )
        except Exception as e:
            print("❌ Vibration error:", e)
            vibration_data = []

    response = {
        "overallHealth": overall_health,
        "detectedClass": label,
        "confidence": round(confidence, 4),
        "classProbabilities": probabilities,
        "issues": issues,
        "vibrationData": vibration_data,
        "timestamp": datetime.now().isoformat(),
        "mode": mode
    }

    # ===============================
    # DEBUG LOG
    # ===============================
    print("=== ANALYSIS RESULT ===")
    print("Label       :", label)
    print("Confidence  :", confidence)
    print("Issues      :", issues)
    print("=======================")

    return response