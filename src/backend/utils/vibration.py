import io

import librosa
import numpy as np
import soundfile as sf

MIN_FREQ_HZ = 20  # abaikan DC / rumble sangat rendah


def generate_vibration_data(wav_bytes: bytes, points: int = 100):
    y, sr = sf.read(io.BytesIO(wav_bytes))
    if y.ndim > 1:
        y = y.mean(axis=1)
    y = y.astype(np.float32)

    if len(y) < 2:
        return []

    n_fft = min(2048, len(y))
    hop = max(1, len(y) // points)

    # Amplitudo: RMS per frame
    rms = librosa.feature.rms(y=y, frame_length=n_fft, hop_length=hop)[0]

    # Frekuensi dominan per frame
    spec = np.abs(librosa.stft(y, n_fft=n_fft, hop_length=hop))
    freqs = librosa.fft_frequencies(sr=sr, n_fft=n_fft)
    mask = freqs >= MIN_FREQ_HZ
    if not mask.any():
        mask = freqs > 0
    dominant = freqs[mask][np.argmax(spec[mask, :], axis=0)]

    n = min(len(rms), len(dominant), points)
    times = librosa.frames_to_time(np.arange(n), sr=sr, hop_length=hop)

    return [
        {
            "time": round(float(times[i]), 4),
            "amplitude": round(float(rms[i]), 6),
            "frequency": round(float(dominant[i]), 2),
        }
        for i in range(n)
    ]