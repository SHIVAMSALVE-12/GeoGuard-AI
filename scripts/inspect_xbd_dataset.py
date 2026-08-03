from datasets import load_dataset

dataset = load_dataset(
    "parquet",
    data_files="backend/datasets/xBD_raw/data/train-00000-of-00017.parquet",
)

print(dataset)
print(dataset["train"].features)

sample = dataset["train"][0]

print("\nKeys:")
print(sample.keys())

print("\nTypes:")
for k, v in sample.items():
    print(k, type(v))