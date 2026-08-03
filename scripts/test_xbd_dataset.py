from backend.datasets.loaders.xbd_dataset import XBDDataset

dataset = XBDDataset()

print("=" * 70)

print("Dataset Size :", len(dataset))

sample = dataset[0]

print()

print(sample["image_name"])

print(sample["pixel_values"].shape)

print(sample["labels"].shape)

print(sample["pixel_values"].dtype)

print(sample["labels"].dtype)

print("=" * 70)