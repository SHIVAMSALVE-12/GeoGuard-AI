"""
GeoGuard AI

Report Service Test

Author: Shivam Salve
"""

from pathlib import Path

from backend.geoguard.engine import GeoGuardEngine
from backend.report.service import ReportService


def main():

    engine = GeoGuardEngine()

    result = engine.predict(

        damage_image=Path(
            "backend/datasets/test_damage.png"
        )

    )

    service = ReportService()

    report = service.generate(result)

    print("=" * 70)

    print("HTML")

    print(report.html_path)

    print()

    print("PDF")

    print(report.pdf_path)

    print("=" * 70)


if __name__ == "__main__":

    main()