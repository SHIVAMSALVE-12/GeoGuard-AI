import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PROJECT_ROOT))

from backend.intelligence.schemas import FloodResult
from backend.intelligence.severity import SeverityEngine

engine = SeverityEngine()

flood = FloodResult(
    flood_detected=True,
    flooded_area_percent=35.0,
)

score, severity = engine.calculate(
    flood=flood
)

print("=" * 60)
print(f"Score    : {score}")
print(f"Severity : {severity}")
print("=" * 60)