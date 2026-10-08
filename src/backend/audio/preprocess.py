import io

import librosa
import numpy as np
import soundfile as sf

# Harus sama persis dengan notebook training
TARGET_SR = 22050
TARGET_DURATION = 4.0


def load_fix_length(y: np.ndarray):
    """
    Sliding window 4 detik, hop 2 detik.
    Audio < 4 detik di-pad, audio panjang di-split menjadi banyak segmen.
    """
    segment_len = int(TARGET_SR * TARGET_DURATION)
    hop_len = segment_len // 2

    if len(y) <= segment_len:
        if len(y) < segment_len:
            y = np.pad(y, (0, segment_len - len(y)))
        return [y]

    segments = []
    for start in range(0, len(y) - segment_len + 1, hop_len):
        segments.append(y[start:start + segment_len])
    return segments


def extract_segment_features(y: np.ndarray) -> np.ndarray:
    features = []

    # MFCC
    mfcc = librosa.feature.mfcc(y=y, sr=TARGET_SR, n_mfcc=13)
    features.extend(mfcc.mean(axis=1))
    features.extend(mfcc.std(axis=1))

    # Delta MFCC
    delta = librosa.feature.delta(mfcc)
    features.extend(delta.mean(axis=1))
    features.extend(delta.std(axis=1))

    # Delta-Delta MFCC
    delta2 = librosa.feature.delta(mfcc, order=2)
    features.extend(delta2.mean(axis=1))
    features.extend(delta2.std(axis=1))

    # Fitur spektral
    features.append(librosa.feature.spectral_centroid(y=y, sr=TARGET_SR).mean())
    features.append(librosa.feature.spectral_bandwidth(y=y, sr=TARGET_SR).mean())
    features.append(librosa.feature.spectral_rolloff(y=y, sr=TARGET_SR).mean())
    features.append(librosa.feature.zero_crossing_rate(y).mean())

    return np.array(features, dtype=np.float32)


def extract_features(wav_bytes: bytes) -> np.ndarray:
    """
    Input : bytes file wav
    Output: array 2D (n_segmen, 82), siap masuk ke SoundModel.predict()
    """
    y, sr = sf.read(io.BytesIO(wav_bytes))

    # Stereo -> mono
    if y.ndim > 1:
        y = y.mean(axis=1)

    y = y.astype(np.float32)

    # Resample ke 22050 Hz seperti saat training
    if sr != TARGET_SR:
        y = librosa.resample(y, orig_sr=sr, target_sr=TARGET_SR)

    segments = load_fix_length(y)
    return np.vstack([extract_segment_features(seg) for seg in segments])