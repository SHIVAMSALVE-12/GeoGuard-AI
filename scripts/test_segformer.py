from transformers import (
    SegformerForSemanticSegmentation,
    SegformerImageProcessor,
)

MODEL_PATH = "backend/models/segformer"

processor = SegformerImageProcessor.from_pretrained(MODEL_PATH)
model = SegformerForSemanticSegmentation.from_pretrained(MODEL_PATH)

print("=" * 50)
print("SegFormer Loaded Successfully!")
print(model.config)
print("=" * 50)