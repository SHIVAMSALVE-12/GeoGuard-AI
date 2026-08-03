"""
GeoGuard AI

Flood Statistics

Author: Shivam Salve
"""

import torch

from backend.intelligence.schemas import (
    FloodResult,
)


class FloodStatistics:
    """
    Compute statistics from a flood prediction mask.
    """

    def __init__(self):

        pass

    def analyze(
        self,
        prediction: torch.Tensor,
    ) -> FloodResult:

        prediction = prediction.cpu()

        total_pixels = prediction.numel()

        flood_pixels = (prediction == 1).sum().item()

        background_pixels = (
            prediction == 0
        ).sum().item()

        flood_percent = (
            flood_pixels / total_pixels
        ) * 100.0

        flood_detected = flood_pixels > 0

        return FloodResult(

            flood_detected=flood_detected,

            flooded_area_percent=round(
                flood_percent,
                2,
            ),

            flood_pixels=flood_pixels,

            background_pixels=background_pixels,
        )