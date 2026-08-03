from pathlib import Path

from backend.inference.damage_predictor import (
    DamagePredictor,
)

from backend.inference.damage_statistics import (
    DamageStatistics,
)

IMAGE = Path(
    "backend/datasets/test_damage.png"
)

predictor = DamagePredictor()

stats = DamageStatistics()

image, prediction = predictor.predict_file(
    IMAGE
)

result = stats.analyze(
    prediction
)

print("=" * 70)

print(result)

print("=" * 70)