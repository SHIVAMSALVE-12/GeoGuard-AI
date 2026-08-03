from pathlib import Path

from backend.inference.flood_infer import (
    FloodInference,
)

IMAGE = Path(
    r"backend/datasets/Sen1Floods11/data/flood_events/HandLabeled/S1Hand/Ghana_103272_S1Hand.tif"
)

engine = FloodInference()

result = engine.predict(
    IMAGE
)

print()

print("=" * 70)

print("Flood AI Result")

print("=" * 70)

print(result)

print("=" * 70)