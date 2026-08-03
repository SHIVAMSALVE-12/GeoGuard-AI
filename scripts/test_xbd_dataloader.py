from backend.training.xbd_dataloader import (
    create_train_loader,
)

loader = create_train_loader()

batch = next(iter(loader))

print("=" * 70)

print(batch["pixel_values"].shape)

print(batch["labels"].shape)

print(batch["labels"].unique())

print("=" * 70)