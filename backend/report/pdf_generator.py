"""
GeoGuard AI

PDF Report Generator

Author: Shivam Salve
"""

from pathlib import Path

from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import (
    Paragraph,
    SimpleDocTemplate,
    Spacer,
)

from backend.report.result import ReportResult


class PDFReportGenerator:
    """
    Generates professional PDF reports.
    """

    def generate(
        self,
        report: ReportResult,
        output_dir="backend/outputs/reports",
    ) -> ReportResult:

        output_dir = Path(output_dir)

        output_dir.mkdir(
            parents=True,
            exist_ok=True,
        )

        pdf_path = output_dir / (
            f"report_{report.report_id}.pdf"
        )

        report.pdf_path = str(pdf_path)

        styles = getSampleStyleSheet()

        document = SimpleDocTemplate(
            str(pdf_path)
        )

        story = []

        # ----------------------------------------
        # Title
        # ----------------------------------------

        story.append(
            Paragraph(
                report.title,
                styles["Title"],
            )
        )

        story.append(
            Spacer(1, 20)
        )

        # ----------------------------------------
        # Metadata
        # ----------------------------------------

        story.append(
            Paragraph(
                f"<b>Report ID:</b> {report.report_id}",
                styles["Normal"],
            )
        )

        story.append(
            Paragraph(
                f"<b>Generated:</b> {report.generated_at}",
                styles["Normal"],
            )
        )

        story.append(
            Spacer(1, 20)
        )

        # ----------------------------------------
        # Executive Summary
        # ----------------------------------------

        story.append(
            Paragraph(
                "<b>Executive Summary</b>",
                styles["Heading2"],
            )
        )

        story.append(
            Paragraph(
                report.reasoning.summary,
                styles["Normal"],
            )
        )

        story.append(
            Spacer(1, 20)
        )

        # ----------------------------------------
        # Situation Analysis
        # ----------------------------------------

        story.append(
            Paragraph(
                "<b>Situation Analysis</b>",
                styles["Heading2"],
            )
        )

        story.append(
            Paragraph(
                report.reasoning.analysis,
                styles["Normal"],
            )
        )

        story.append(
            Spacer(1, 20)
        )

        # ----------------------------------------
        # Assessment
        # ----------------------------------------

        story.append(
            Paragraph(
                "<b>Assessment</b>",
                styles["Heading2"],
            )
        )

        story.append(
            Paragraph(
                f"Severity : {report.assessment.severity}",
                styles["Normal"],
            )
        )

        story.append(
            Paragraph(
                f"Impact : {report.assessment.impact}",
                styles["Normal"],
            )
        )

        story.append(
            Paragraph(
                f"Confidence : {report.assessment.confidence:.1f}%",
                styles["Normal"],
            )
        )

        story.append(
            Spacer(1, 20)
        )

        # ----------------------------------------
        # Damage Statistics
        # ----------------------------------------

        story.append(
            Paragraph(
                "<b>Damage Statistics</b>",
                styles["Heading2"],
            )
        )

        for key, value in report.assessment.damage.items():

            story.append(
                Paragraph(
                    f"{key}: {value:.2f}%",
                    styles["Normal"],
                )
            )

        story.append(
            Spacer(1, 20)
        )

        # ----------------------------------------
        # Recommendations
        # ----------------------------------------

        story.append(
            Paragraph(
                "<b>Recommendations</b>",
                styles["Heading2"],
            )
        )

        for recommendation in report.reasoning.recommendations:

            story.append(
                Paragraph(
                    f"• {recommendation}",
                    styles["Normal"],
                )
            )

        story.append(
            Spacer(1, 20)
        )

        # ----------------------------------------
        # Priority
        # ----------------------------------------

        story.append(
            Paragraph(
                "<b>Priority Level</b>",
                styles["Heading2"],
            )
        )

        story.append(
            Paragraph(
                report.reasoning.priority,
                styles["Normal"],
            )
        )

        document.build(
            story
        )

        print(
            f"✅ PDF Saved -> {report.pdf_path}"
        )

        return report