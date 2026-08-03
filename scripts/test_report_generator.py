"""
GeoGuard AI

Professional Report Generator Test

Author: Shivam Salve
"""

from pathlib import Path

from backend.geoguard.engine import GeoGuardEngine

from backend.report.result import ReportResult

from backend.report.generator import ReportGenerator

from backend.report.pdf_generator import PDFReportGenerator

from backend.report.image_manager import ImageManager

from backend.report.charts import ChartGenerator


def divider(title: str):

    print("\n" + "=" * 70)

    print(title)

    print("=" * 70)


def main():

    # =====================================================
    # Run GeoGuard AI
    # =====================================================

    divider("Initializing GeoGuard AI")

    engine = GeoGuardEngine()

    geo_result = engine.predict(

        damage_image=Path(
            "backend/datasets/test_damage.png"
        )

    )

    # =====================================================
    # Create Report Object
    # =====================================================

    divider("Preparing Report")

    report = ReportResult()

    report.assessment = geo_result.assessment

    report.reasoning = geo_result.reasoning

    # -----------------------------------------------------
    # Report Metadata
    # -----------------------------------------------------

    report.disaster_type = (
        "Building Damage Assessment"
    )

    report.location = (
        "Sample Test Dataset"
    )

    report.satellite = (
        "High Resolution Satellite"
    )

    report.analyst = (
        "GeoGuard AI"
    )

    report.organization = (
        "GeoGuard AI Platform"
    )

    report.notes = [

        "This report is automatically generated.",

        "Predictions are AI-assisted.",

        "Human verification is recommended.",

    ]

    # =====================================================
    # Collect AI Images
    # =====================================================

    divider("Collecting Images")

    report.images = ImageManager.collect(
        geo_result
    )

    # =====================================================
    # Generate Charts
    # =====================================================

    divider("Generating Charts")

    charts = ChartGenerator()

    report.damage_chart = (
        charts.damage_chart(
            report.assessment
        )
    )

    report.flood_chart = (
        charts.flood_chart(
            report.assessment
        )
    )

    report.landcover_chart = (
        charts.landcover_chart(
            report.assessment
        )
    )

    report.confidence_chart = (
        charts.confidence_chart(
            report.assessment
        )
    )

    # =====================================================
    # Generate HTML Report
    # =====================================================

    divider("Generating HTML Report")

    html = ReportGenerator()

    report = html.generate(
        report
    )

    # =====================================================
    # Generate PDF Report
    # =====================================================

    divider("Generating PDF Report")

    pdf = PDFReportGenerator()

    report = pdf.generate(
        report
    )

    # =====================================================
    # Output Summary
    # =====================================================

    divider("Generated Files")

    print("HTML Report")

    print(report.html_path)

    print()

    print("PDF Report")

    print(report.pdf_path)

    print()

    print("Collected Images")

    if report.images:

        for key, value in report.images.items():

            print(
                f"{key:<25}: {value}"
            )

    else:

        print("No images collected.")

    print()

    print("Generated Charts")

    print(
        f"Damage Chart      : {report.damage_chart}"
    )

    print(
        f"Flood Chart       : {report.flood_chart}"
    )

    print(
        f"LandCover Chart   : {report.landcover_chart}"
    )

    print(
        f"Confidence Chart  : {report.confidence_chart}"
    )

    divider("Assessment")

    print(report.assessment)

    divider("Reasoning")

    print("Summary")

    print(report.reasoning.summary)

    print()

    print("Priority")

    print(report.reasoning.priority)

    print()

    print("Recommendations")

    if report.reasoning.recommendations:

        for i, recommendation in enumerate(

            report.reasoning.recommendations,

            start=1,

        ):

            print(
                f"{i}. {recommendation}"
            )

    else:

        print("No recommendations.")

    divider("SUCCESS")

    print(
        "Professional HTML Report Generated Successfully!"
    )

    print(
        "Professional PDF Report Generated Successfully!"
    )

    print(
        "GeoGuard AI Professional Report Pipeline Completed."
    )


if __name__ == "__main__":

    main()