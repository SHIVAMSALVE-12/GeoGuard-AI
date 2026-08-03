from pathlib import Path

from backend.inference.damage_predictor import (
    DamagePredictor,
)

from backend.inference.damage_visualizer import (
    DamageVisualizer,
)

IMAGE = Path(
    "backend/datasets/test_damage.png"
)

predictor = DamagePredictor()

visualizer = DamageVisualizer()

image, prediction = predictor.predict_file(
    IMAGE
)

visualizer.save_prediction(
    prediction
)

visualizer.save_overlay(
    image,
    prediction
)

print("=" * 60)

print("Visualization Completed")

print("=" * 60)