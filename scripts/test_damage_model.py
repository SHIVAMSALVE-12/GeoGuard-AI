from backend.models.damage_segformer import (
    build_damage_segformer,
)

model = build_damage_segformer()

print("=" * 70)

print(type(model))

print(model.config.num_labels)

print(model.decode_head.classifier.weight.shape)

print("=" * 70)