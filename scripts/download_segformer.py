from pathlib import Path
from transformers import (
    SegformerImageProcessor,
    SegformerForSemanticSegmentation,
)

MODEL_NAME = "nvidia/segformer-b2-finetuned-ade-512-512"
SAVE_DIR = Path("backend/models/segformer")

print("=" * 60)
print("Downloading SegFormer-B2...")
print("=" * 60)

# Download processor
processor = SegformerImageProcessor.from_pretrained(MODEL_NAME)

# Download model
model = SegformerForSemanticSegmentation.from_pretrained(MODEL_NAME)

# Save locally
processor.save_pretrained(SAVE_DIR)
model.save_pretrained(SAVE_DIR)

print("\n✅ SegFormer downloaded successfully!")
print(f"Model saved to: {SAVE_DIR.resolve()}")