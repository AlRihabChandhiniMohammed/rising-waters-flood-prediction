"""
Prediction Module — Rising-Waters-Flood-Prediction

Loads a trained model and generates predictions on new input data.
"""

import joblib
import numpy as np

def load_model(filepath):
    """Deserialize a trained model from disk."""
    return joblib.load(filepath)


def predict_single(model, features):
    """Predict flood risk for a single input sample."""
    feat_arr = np.array(features).reshape(1, -1)
    return int(model.predict(feat_arr)[0])


def predict_batch(model, feature_matrix):
    """Predict flood risk for a batch of samples."""
    feat_arr = np.array(feature_matrix)
    return model.predict(feat_arr).tolist()


def predict_proba(model, features):
    """Return probability scores for each class."""
    feat_arr = np.array(features)
    if len(feat_arr.shape) == 1:
        feat_arr = feat_arr.reshape(1, -1)
        return model.predict_proba(feat_arr)[0].tolist()
    return model.predict_proba(feat_arr).tolist()

