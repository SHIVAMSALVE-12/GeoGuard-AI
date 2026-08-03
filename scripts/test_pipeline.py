import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PROJECT_ROOT))

from backend.intelligence.schemas import (
    LandCoverResult,
    FloodResult,
)

from backend.intelligence.pipeline import (
    DisasterPipeline,
)

land = LandCoverResult(
    dominant_class="Tree",
    percentages={
        "Tree": 42,
        "Water": 18,
    },
    pixel_counts={},
)

flood = FloodResult(
    flood_detected=True,
    flooded_area_percent=28.4,
)

pipeline = DisasterPipeline()

result = pipeline.run(
    land_cover=land,
    flood=flood,
)

print("=" * 70)

print(result["assessment"])

print("=" * 70)

print(result["report"])