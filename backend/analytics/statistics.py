"""
GeoGuard AI

Statistics Engine

Author: Shivam Salve
"""

import json
from pathlib import Path

import numpy as np

from backend.config.classes import CLASS_NAMES


class StatisticsGenerator:
    """
    Generates statistics from a segmentation mask.
    """

    def __init__(self):
        pass

    def compute(self, prediction):

        mask = prediction.numpy()

        total_pixels = mask.size

        stats = {}

        pixel_counts = {}

        percentages = {}

        unique = np.unique(mask)

        for class_id in unique:

            count = int((mask == class_id).sum())

            percentage = (
                count / total_pixels
            ) * 100

            class_name = CLASS_NAMES.get(
                int(class_id),
                f"Class_{class_id}"
            )

            pixel_counts[class_name] = count

            percentages[class_name] = round(
                percentage,
                2,
            )

        dominant = max(
            percentages,
            key=percentages.get,
        )

        stats["width"] = mask.shape[1]

        stats["height"] = mask.shape[0]

        stats["total_pixels"] = total_pixels

        stats["dominant_class"] = dominant

        stats["pixel_counts"] = pixel_counts

        stats["percentages"] = percentages

        return stats

    def save_json(
        self,
        stats,
        output_path,
    ):

        output_path = Path(output_path)

        output_path.parent.mkdir(
            parents=True,
            exist_ok=True,
        )

        with open(
            output_path,
            "w",
        ) as file:

            json.dump(
                stats,
                file,
                indent=4,
            )

        print(
            f"✅ Statistics saved -> {output_path}"
        )