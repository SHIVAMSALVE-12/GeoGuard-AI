from backend.datasets.loaders.xbd_dataset import XBDDataset
from backend.datasets.transforms.xbd import get_train_transform

dataset = XBDDataset(
    transform=get_train_transform()
)

sample = dataset[0]

print("=" * 70)

print(sample["pixel_values"].shape)
print(sample["labels"].shape)

print("=" * 70)