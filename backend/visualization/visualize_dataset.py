"""
Dataset Visualization Module
"""

import matplotlib.pyplot as plt
import numpy as np


from backend.visualization.overlay import (
    colorize_mask,
    create_overlay,
)


def visualize_sample(sample):

    image = sample["pixel_values"]

    mask = sample["labels"]

    if hasattr(image, "numpy"):
        image = image.permute(1, 2, 0).numpy()

    if hasattr(mask, "numpy"):
        mask = mask.numpy()

    # Undo normalization
    mean = np.array([0.485, 0.456, 0.406])
    std = np.array([0.229, 0.224, 0.225])

    image = image * std + mean

    image = np.clip(image, 0, 1)

    image = (image * 255).astype(np.uint8)

    color_mask = colorize_mask(mask)

    overlay = create_overlay(image, color_mask)

    fig, ax = plt.subplots(1, 4, figsize=(20, 6))

    ax[0].imshow(image)
    ax[0].set_title("Image")

    ax[1].imshow(mask)
    ax[1].set_title("Mask")

    ax[2].imshow(color_mask)
    ax[2].set_title("Color Mask")

    ax[3].imshow(overlay)
    ax[3].set_title("Overlay")

    for a in ax:
        a.axis("off")

    plt.tight_layout()

    plt.show()