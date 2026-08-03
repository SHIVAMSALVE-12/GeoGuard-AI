from pathlib import Path

from backend.inference.flood_preprocess import (
    preprocess_flood_image,
)

from backend.inference.flood_predictor import (
    FloodPredictor,
)

from backend.inference.flood_statistics import (
    FloodStatistics,
)

IMAGE = Path(
    r"backend/datasets/Sen1Floods11/data/flood_events/HandLabeled/S1Hand/Ghana_103272_S1Hand.tif"
)

_, tensor = preprocess_flood_image(
    IMAGE
)

predictor = FloodPredictor()

prediction = predictor.predict(
    tensor
)

stats = FloodStatistics()

result = stats.analyze(
    prediction
)

print("=" * 60)

print(result)

print("=" * 60)