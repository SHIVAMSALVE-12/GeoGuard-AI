import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PROJECT_ROOT))

from backend.intelligence.schemas import FloodResult
from backend.intelligence.recommendation import RecommendationEngine

engine = RecommendationEngine()

flood = FloodResult(
    flood_detected=True,
    flooded_area_percent=34.6,
)

recommendations = engine.generate(
    flood=flood
)

print("=" * 60)

for i, recommendation in enumerate(recommendations, start=1):
    print(f"{i}. {recommendation}")

print("=" * 60)