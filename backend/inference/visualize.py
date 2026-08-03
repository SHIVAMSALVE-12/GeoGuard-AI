"""
GeoGuard AI

Visualization Engine
"""

from pathlib import Path

import numpy as np

from PIL import Image

from backend.inference.color_map import colorize_mask


class Visualizer:

    def __init__(self):
        pass

    def save_prediction(
        self,
        prediction,
        output_path,
    ):
        """
        Save the colored segmentation mask.
        """

        rgb = colorize_mask(
            prediction.numpy()
        )

        image = Image.fromarray(rgb)

        output_path = Path(output_path)

        output_path.parent.mkdir(
            parents=True,
            exist_ok=True,
        )

        image.save(output_path)

        print(f"✅ Prediction saved -> {output_path}")

    def save_overlay(
        self,
        original_image,
        prediction,
        output_path,
        alpha=0.45,
    ):
        """
        Blend prediction with original image.
        """

        rgb_mask = colorize_mask(
            prediction.numpy()
        )

        mask_image = Image.fromarray(rgb_mask)

        original = original_image.convert("RGB")

        overlay = Image.blend(
            original,
            mask_image,
            alpha,
        )

        output_path = Path(output_path)

        output_path.parent.mkdir(
            parents=True,
            exist_ok=True,
        )

        overlay.save(output_path)

        print(f"✅ Overlay saved -> {output_path}")