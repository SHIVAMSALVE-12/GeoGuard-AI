import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PROJECT_ROOT))

from backend.models.segformer_model import build_segformer

model = build_segformer()

print("=" * 60)

print(model)

print()

print("Number of Classes :", model.config.num_labels)

print("=" * 60)