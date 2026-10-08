import os
import joblib
import numpy as np

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

MODEL_PATH = os.path.join(BASE_DIR, "xgb_model.joblib")
SCALER_PATH = os.path.join(BASE_DIR, "feature_scaler.joblib")
LABEL_MAP_PATH = os.path.join(BASE_DIR, "label_map.joblib")


class SoundModel:
    def __init__(self):
        self.model = joblib.load(MODEL_PATH)
        self.scaler = joblib.load(SCALER_PATH)
        self.label_map = joblib.load(LABEL_MAP_PATH)  # {label: index}

        # Urutan label sesuai index output model
        self.classes = [
            label for label, _ in sorted(self.label_map.items(), key=lambda x: x[1])
        ]

    def predict(self, features: np.ndarray) -> np.ndarray:
        """
        features: array 2D (n_segmen, n_fitur) hasil extract_features per segmen.
        Return: probabilitas (n_segmen, n_kelas).
        """
        features = np.asarray(features, dtype=np.float32)
        if features.ndim == 1:
            features = features.reshape(1, -1)

        scaled = self.scaler.transform(features)
        return self.model.predict_proba(scaled)