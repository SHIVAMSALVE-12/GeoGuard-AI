from pathlib import Path

from backend.inference.flood_preprocess import (
    preprocess_flood_image,
)

from backend.inference.flood_predictor import (
    FloodPredictor,
)

from backend.inference.flood_visualizer import (
    FloodVisualizer,
)

IMAGE = Path(
    r"backend/datasets/Sen1Floods11/data/flood_events/HandLabeled/S1Hand/Ghana_103272_S1Hand.tif"
)

original, tensor = preprocess_flood_image(
    IMAGE
)

predictor = FloodPredictor()

prediction = predictor.predict(
    tensor
)

visualizer = FloodVisualizer()

visualizer.save_prediction(
    prediction
)

visualizer.save_overlay(
    original,
    prediction,
)