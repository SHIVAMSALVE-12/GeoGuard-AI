from pathlib import Path

from backend.inference.damage_inference import (
    DamageInference,
)

IMAGE = Path(
    "backend/datasets/test_damage.png"
)

pipeline = DamageInference()

result = pipeline.predict(
    IMAGE
)

print("=" * 70)

print(result.statistics)

print()

print(
    "Prediction File:",
    result.prediction_path,
)

print()

print(
    "Overlay File:",
    result.overlay_path,
)

print("=" * 70)