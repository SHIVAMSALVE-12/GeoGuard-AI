"""
GeoGuard AI

Professional Report Result

Author: Shivam Salve
"""

from dataclasses import dataclass, field

from backend.assessment.result import AssessmentResult
from backend.reasoning.result import ReasoningResult


@dataclass
class ReportResult:
    """
    Complete professional disaster report.

    This object stores everything required
    to generate HTML/PDF reports and
    expose report data through the API.
    """

    # =====================================================
    # Report Information
    # =====================================================

    title: str = "GeoGuard AI Disaster Assessment Report"

    report_id: str = ""

    generated_at: str = ""

    version: str = "1.0"

    author: str = "GeoGuard AI"

    # =====================================================
    # AI Results
    # =====================================================

    assessment: AssessmentResult | None = None

    reasoning: ReasoningResult | None = None

    # =====================================================
    # AI Generated Images
    # =====================================================

    images: dict[str, str] = field(
        default_factory=dict
    )

    landcover_image: str = ""

    flood_image: str = ""

    damage_image: str = ""

    overlay_image: str = ""

    # =====================================================
    # Generated Charts
    # =====================================================

    damage_chart: str = ""

    flood_chart: str = ""

    landcover_chart: str = ""

    confidence_chart: str = ""

    # =====================================================
    # Export Files
    # =====================================================

    html_path: str = ""

    pdf_path: str = ""

    # =====================================================
    # Additional Notes
    # =====================================================

    notes: list[str] = field(
        default_factory=list
    )

    # =====================================================
    # Report Metadata
    # =====================================================

    disaster_type: str = "Unknown"

    location: str = "Unknown"

    satellite: str = "Unknown"

    analyst: str = "GeoGuard AI"

    organization: str = "GeoGuard AI Platform"