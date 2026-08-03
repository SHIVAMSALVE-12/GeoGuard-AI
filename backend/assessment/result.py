"""
GeoGuard AI

Disaster Assessment Result

Author: Shivam Salve
"""

from dataclasses import dataclass, field


@dataclass
class AssessmentResult:
    """
    Unified disaster assessment generated from all AI modules.
    """

    # -------------------------------------------------
    # AI Statistics
    # -------------------------------------------------

    landcover: dict[str, float] = field(default_factory=dict)

    flood: dict[str, float] = field(default_factory=dict)

    damage: dict[str, float] = field(default_factory=dict)

    # -------------------------------------------------
    # Overall Assessment
    # -------------------------------------------------

    severity: str = "Unknown"

    impact: str = "Unknown"

    confidence: float = 0.0

    summary: str = ""

    recommendations: list[str] = field(default_factory=list)