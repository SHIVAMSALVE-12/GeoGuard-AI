import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PROJECT_ROOT))

from backend.intelligence.schemas import (
    LandCoverResult,
    FloodResult,
)

from backend.intelligence.fusion import FusionEngine
from backend.intelligence.reasoning import AIReasoningEngine
from backend.intelligence.report import DisasterReportGenerator

# --------------------------------------------------

land = LandCoverResult(
    dominant_class="Tree",
    percentages={"Tree": 42},
    pixel_counts={},
)

flood = FloodResult(
    flood_detected=True,
    flooded_area_percent=28.4,
)

fusion = FusionEngine()

fused = fusion.fuse(
    land_cover=land,
    flood=flood,
)

reasoning = AIReasoningEngine()

assessment = reasoning.analyze(fused)

report_engine = DisasterReportGenerator()

report = report_engine.generate(
    assessment,
    land,
)

report_engine.save(
    report,
    "backend/outputs/disaster_report.txt",
)

print(report)