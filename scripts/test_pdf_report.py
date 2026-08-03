from pathlib import Path

from backend.geoguard.engine import GeoGuardEngine
from backend.report.generator import ReportGenerator
from backend.report.pdf_generator import PDFReportGenerator
from backend.report.result import ReportResult


engine = GeoGuardEngine()

geo = engine.predict(
    damage_image=Path(
        "backend/datasets/test_damage.png"
    )
)

report = ReportResult()

report.assessment = geo.assessment
report.reasoning = geo.reasoning

html = ReportGenerator()

report = html.generate(report)

pdf = PDFReportGenerator()

report = pdf.generate(report)

print("=" * 70)

print(report.pdf_path)

print("=" * 70)