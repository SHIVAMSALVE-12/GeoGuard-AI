"""
GeoGuard AI

Unified GeoGuard Result

Author: Shivam Salve
"""

from dataclasses import dataclass
from typing import Any


@dataclass
class GeoGuardResult:
    """
    Unified result returned by GeoGuardEngine.

    This object stores the outputs from all AI modules
    together with the disaster assessment, AI reasoning,
    and generated reports.
    """

    # ==================================================
    # Raw AI Outputs
    # ==================================================

    landcover: Any = None

    flood: Any = None

    damage: Any = None

    # ==================================================
    # Disaster Assessment
    # ==================================================

    assessment: Any = None

    # ==================================================
    # AI Reasoning
    # ==================================================

    reasoning: Any = None

    # ==================================================
    # Generated Report
    # ==================================================

    report: Any = None