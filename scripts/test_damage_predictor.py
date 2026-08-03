from pathlib import Path

from backend.inference.damage_predictor import (
    DamagePredictor,
)

IMAGE = Path(
    "backend/datasets/test_damage.png"
)

predictor = DamagePredictor()

image, prediction = predictor.predict_file(
    IMAGE
)

print("=" * 60)

print(
    "Prediction Shape:",
    prediction.shape,
)

print(
    "Unique Classes:",
    prediction.unique(),
)

print("=" * 60)