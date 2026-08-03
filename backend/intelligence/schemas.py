"""
GeoGuard AI

Disaster Intelligence Schemas

Author: Shivam Salve
"""

from dataclasses import dataclass, field


@dataclass
class LandCoverResult:

    dominant_class: str

    percentages: dict

    pixel_counts: dict


@dataclass
class FloodResult:

    flood_detected: bool = False

    flooded_area_percent: float = 0.0

    flood_pixels: int = 0

    background_pixels: int = 0


@dataclass
class DamageResult:

    buildings_damaged: int = 0

    damage_level: str = "None"


@dataclass
class ChangeDetectionResult:

    change_detected: bool = False

    changed_area_percent: float = 0.0


@dataclass
class DisasterAssessment:

    severity: str = "Unknown"

    risk_score: float = 0.0

    summary: str = ""

    recommendations: list = field(default_factory=list)