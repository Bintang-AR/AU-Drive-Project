import os
import subprocess
import tempfile


def webm_to_wav(webm_bytes: bytes) -> bytes:
    with tempfile.NamedTemporaryFile(delete=False, suffix=".webm") as webm_file:
        webm_file.write(webm_bytes)
        webm_path = webm_file.name

    wav_path = webm_path[: -len(".webm")] + ".wav"

    try:
        subprocess.run(
            ["ffmpeg", "-y", "-i", webm_path, "-ac", "1", wav_path],
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
            check=True,
        )
        with open(wav_path, "rb") as f:
            return f.read()
    finally:
        for p in (webm_path, wav_path):
            if os.path.exists(p):
                os.remove(p)