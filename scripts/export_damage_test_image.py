from datasets import load_dataset
import numpy as np
from PIL import Image

dataset = load_dataset(
    "parquet",
    data_files="backend/datasets/xBD_raw/data/test-00000-of-00006.parquet",
)

sample = dataset["train"][0]

image = np.array(sample["t2_image"])

Image.fromarray(image).save(
    "backend/datasets/test_damage.png"
)

print("Saved test image!")