import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PROJECT_ROOT))

from backend.intelligence.schemas import (
    LandCoverResult,
    FloodResult,
)

from backend.intelligence.fusion import (
    FusionEngine,
)

from backend.intelligence.reasoning import (
    AIReasoningEngine,
)

# --------------------------------------------------
# Create mock model outputs
# --------------------------------------------------

land = LandCoverResult(
    dominant_class="Tree",
    percentages={
        "Tree": 42.0,
        "Water": 15.0,
    },
    pixel_counts={},
)

flood = FloodResult(
    flood_detected=True,
    flooded_area_percent=28.4,
)

# --------------------------------------------------
# Fuse results
# --------------------------------------------------

fusion = FusionEngine()

fused_results = fusion.fuse(
    land_cover=land,
    flood=flood,
)

# --------------------------------------------------
# Run reasoning
# --------------------------------------------------

engine = AIReasoningEngine()

assessment = engine.analyze(fused_results)

print("=" * 60)
print(assessment)
print("=" * 60)