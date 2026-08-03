from pathlib import Path

import torch

from backend.inference.flood_preprocess import (
    preprocess_flood_image,
)

from backend.inference.flood_predictor import (
    FloodPredictor,
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

print("=" * 60)

print("Prediction Shape :", prediction.shape)

print("Unique Classes   :", torch.unique(prediction))

print("=" * 60)