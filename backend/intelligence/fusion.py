"""
GeoGuard AI

Multi-Model Fusion Engine

Author: Shivam Salve
"""

from backend.intelligence.schemas import (
    LandCoverResult,
    FloodResult,
    DamageResult,
    ChangeDetectionResult,
)


class FusionEngine:
    """
    Combines outputs from multiple AI models into
    a single dictionary for reasoning.
    """

    def __init__(self):
        pass

    def fuse(
        self,
        land_cover: LandCoverResult,
        flood: FloodResult | None = None,
        damage: DamageResult | None = None,
        change: ChangeDetectionResult | None = None,
    ):

        return {

            "land_cover": land_cover,

            "flood": flood,

            "damage": damage,

            "change": change,

        }