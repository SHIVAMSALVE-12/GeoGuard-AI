import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PROJECT_ROOT))

from backend.inference.predictor import SegFormerPredictor

print("=" * 60)

predictor = SegFormerPredictor()

print("=" * 60)

print("Predictor Loaded Successfully!")

print("=" * 60)