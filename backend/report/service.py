"""
GeoGuard AI

Report Service

Author: Shivam Salve
"""

from backend.geoguard.result import GeoGuardResult
from backend.report.charts import ChartGenerator
from backend.report.generator import ReportGenerator
from backend.report.image_manager import ImageManager
from backend.report.pdf_generator import PDFReportGenerator
from backend.report.result import ReportResult


class ReportService:
    """
    Generates complete HTML and PDF reports
    from a GeoGuardResult.
    """

    def __init__(self):

        self.chart_generator = ChartGenerator()

        self.html_generator = ReportGenerator()

        self.pdf_generator = PDFReportGenerator()

    def generate(
        self,
        geoguard_result: GeoGuardResult,
    ) -> ReportResult:

        report = ReportResult()

        # -------------------------------------------------
        # AI Results
        # -------------------------------------------------

        report.assessment = geoguard_result.assessment

        report.reasoning = geoguard_result.reasoning

        # -------------------------------------------------
        # Metadata
        # -------------------------------------------------

        report.disaster_type = "Disaster Assessment"

        report.location = "Unknown"

        report.satellite = "Unknown"

        report.analyst = "GeoGuard AI"

        report.organization = "GeoGuard AI Platform"

        # -------------------------------------------------
        # Images
        # -------------------------------------------------

        report.images = ImageManager.collect(
            geoguard_result
        )

        # -------------------------------------------------
        # Charts
        # -------------------------------------------------

        report.damage_chart = (
            self.chart_generator.damage_chart(
                report.assessment
            )
        )

        report.flood_chart = (
            self.chart_generator.flood_chart(
                report.assessment
            )
        )

        report.landcover_chart = (
            self.chart_generator.landcover_chart(
                report.assessment
            )
        )

        report.confidence_chart = (
            self.chart_generator.confidence_chart(
                report.assessment
            )
        )

        # -------------------------------------------------
        # HTML
        # -------------------------------------------------

        report = self.html_generator.generate(
            report
        )

        # -------------------------------------------------
        # PDF
        # -------------------------------------------------

        report = self.pdf_generator.generate(
            report
        )

        return report