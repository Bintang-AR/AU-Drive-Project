import numpy as np

from models.predictor import SoundModel
from audio.preprocess import extract_features

model = SoundModel()
CLASSES = model.classes


def run_inference(wav_bytes: bytes):
    features = extract_features(wav_bytes)          # (n_segmen, 82)
    probs = model.predict(features)                 # (n_segmen, n_kelas)

    if probs.ndim != 2 or probs.shape[1] != len(CLASSES):
        raise ValueError(f"Output model tidak valid: {probs.shape}")

    seg_preds = np.argmax(probs, axis=1)
    votes = np.bincount(seg_preds, minlength=len(CLASSES))
    mean_probs = probs.mean(axis=0)

    candidates = np.where(votes == votes.max())[0]
    class_index = int(candidates[np.argmax(mean_probs[candidates])])

    label = CLASSES[class_index]
    confidence = float(mean_probs[class_index])
    probabilities = {
        CLASSES[i]: round(float(mean_probs[i]), 4) for i in range(len(CLASSES))
    }
    return label, confidence, probabilities