"""
GeoGuard AI

Professional HTML Report Generator

Author: Shivam Salve
"""

from datetime import datetime
from pathlib import Path
from uuid import uuid4

from backend.report.result import ReportResult


class ReportGenerator:
    """
    Generates a professional disaster assessment
    HTML report.
    """

    def generate(
        self,
        report: ReportResult,
        output_dir: str = "backend/outputs/reports",
    ) -> ReportResult:

        output_dir = Path(output_dir)

        output_dir.mkdir(
            parents=True,
            exist_ok=True,
        )

        # -----------------------------------------
        # Metadata
        # -----------------------------------------

        report.generated_at = datetime.now().strftime(
            "%d-%m-%Y %H:%M:%S"
        )

        report.report_id = str(
            uuid4()
        )[:8]

        filename = (
            f"report_{report.report_id}.html"
        )

        report.html_path = str(
            output_dir / filename
        )

        html = self._build_html(
            report
        )

        with open(
            report.html_path,
            "w",
            encoding="utf-8",
        ) as f:

            f.write(html)

        print(
            f"✅ Report Saved -> {report.html_path}"
        )

        return report

    # ============================================================
    # HTML Builder
    # ============================================================

    def _build_html(
        self,
        report: ReportResult,
    ) -> str:

        assessment = report.assessment

        reasoning = report.reasoning

        # -------------------------------------------------------
        # Severity Badge Color
        # -------------------------------------------------------

        severity_color = {

            "Low": "#2ecc71",

            "Moderate": "#f1c40f",

            "High": "#e67e22",

            "Critical": "#e74c3c",

        }.get(
            assessment.severity if assessment else "",
            "#3498db",
        )

        # -------------------------------------------------------
        # HTML
        # -------------------------------------------------------

        html = f"""
<!DOCTYPE html>

<html>

<head>

<meta charset="utf-8">

<title>{report.title}</title>

<style>

body {{

background:#edf2f7;

font-family:Arial,Helvetica,sans-serif;

margin:0;

padding:40px;

}}

.container {{

max-width:1200px;

margin:auto;

background:white;

padding:40px;

border-radius:12px;

box-shadow:0px 3px 10px rgba(0,0,0,.15);

}}

.cover {{

text-align:center;

margin-bottom:40px;

}}

.cover h1 {{

font-size:42px;

color:#0b5394;

margin-bottom:5px;

}}

.cover h2 {{

color:#666666;

margin-top:0;

}}

hr {{

margin-top:25px;

margin-bottom:25px;

}}

table {{

width:100%;

border-collapse:collapse;

margin-top:20px;

margin-bottom:30px;

}}

th,td {{

border:1px solid #dddddd;

padding:12px;

}}

th {{

background:#f2f2f2;

width:220px;

}}

.section {{

margin-top:45px;

}}

.cards {{

display:flex;

gap:20px;

margin-top:20px;

margin-bottom:30px;

}}

.metric {{

flex:1;

background:#f5f7fa;

padding:20px;

border-radius:10px;

text-align:center;

box-shadow:0px 1px 5px rgba(0,0,0,.1);

}}

.metric h3 {{

margin:0;

color:#444;

}}

.metric p {{

font-size:24px;

font-weight:bold;

margin-top:15px;

}}

.badge {{

padding:18px;

border-radius:10px;

text-align:center;

font-size:24px;

font-weight:bold;

color:white;

background:{severity_color};

margin-top:15px;

}}

.card {{

margin-top:25px;

margin-bottom:35px;

}}

.report-image {{

width:700px;

max-width:100%;

border-radius:8px;

border:1px solid #bbbbbb;

}}

.footer {{

margin-top:60px;

text-align:center;

font-size:13px;

color:#777777;

}}

</style>

</head>

<body>

<div class="container">

<!-- ====================================================== -->
<!-- COVER PAGE -->
<!-- ====================================================== -->

<div class="cover">

<h1>GeoGuard AI</h1>

<h2>Disaster Assessment Report</h2>

</div>

<table>

<tr>

<th>Report ID</th>

<td>{report.report_id}</td>

</tr>

<tr>

<th>Generated</th>

<td>{report.generated_at}</td>

</tr>

<tr>

<th>Disaster</th>

<td>{report.disaster_type}</td>

</tr>

<tr>

<th>Location</th>

<td>{report.location}</td>

</tr>

<tr>

<th>Satellite</th>

<td>{report.satellite}</td>

</tr>

<tr>

<th>Organization</th>

<td>{report.organization}</td>

</tr>

<tr>

<th>Analyst</th>

<td>{report.analyst}</td>

</tr>

<tr>

<th>Version</th>

<td>{report.version}</td>

</tr>

</table>

<hr>
"""
                # ======================================================
        # Executive Summary
        # ======================================================

        html += f"""

<div class="section">

<h2>Executive Summary</h2>

<p>

{reasoning.summary if reasoning else ""}

</p>

</div>

"""

        # ======================================================
        # Summary Cards
        # ======================================================

        html += f"""

<div class="cards">

<div class="metric">

<h3>Impact</h3>

<p>

{assessment.impact if assessment else ""}

</p>

</div>

<div class="metric">

<h3>Confidence</h3>

<p>

{f"{assessment.confidence:.1f}%" if assessment else "0%"}

</p>

</div>

<div class="metric">

<h3>Priority</h3>

<p>

{reasoning.priority if reasoning else ""}

</p>

</div>

</div>

"""

        # ======================================================
        # Severity Badge
        # ======================================================

        html += f"""

<div class="section">

<h2>Overall Severity</h2>

<div class="badge">

{assessment.severity if assessment else ""}

</div>

</div>

"""

        # ======================================================
        # Situation Analysis
        # ======================================================

        html += f"""

<div class="section">

<h2>Situation Analysis</h2>

<p>

{reasoning.analysis if reasoning else ""}

</p>

</div>

"""

        # ======================================================
        # AI Images
        # ======================================================

        html += """

<div class="section">

<h2>AI Generated Images</h2>

"""

        for title, path in report.images.items():

            if not path:
                continue

            image_path = Path(path).as_posix()

            html += f"""

<div class="card">

<h3>{title.replace("_", " ").title()}</h3>

<img
src="../{image_path}"
class="report-image"
>

</div>

"""

        html += """

</div>

"""

        # ======================================================
        # AI Charts
        # ======================================================

        html += """

<div class="section">

<h2>AI Statistics</h2>

"""

        charts = {

            "Damage Distribution":
                report.damage_chart,

            "Flood Distribution":
                report.flood_chart,

            "Land Cover Distribution":
                report.landcover_chart,

            "AI Confidence":
                report.confidence_chart,

        }

        for title, path in charts.items():

            if not path:
                continue

            chart_path = Path(path).as_posix()

            html += f"""

<div class="card">

<h3>{title}</h3>

<img
src="../{chart_path}"
class="report-image"
>

</div>

"""

        html += """

</div>

"""

        # ======================================================
        # Assessment
        # ======================================================

        html += f"""

<div class="section">

<h2>Assessment</h2>

<table>

<tr>

<th>Severity</th>

<td>

{assessment.severity if assessment else ""}

</td>

</tr>

<tr>

<th>Impact</th>

<td>

{assessment.impact if assessment else ""}

</td>

</tr>

<tr>

<th>Confidence</th>

<td>

{f"{assessment.confidence:.1f}%" if assessment else "0%"}


</td>

</tr>

</table>

</div>

"""

        # ======================================================
        # Damage Statistics
        # ======================================================

        html += """

<div class="section">

<h2>Building Damage Statistics</h2>

<table>

<tr>

<th>Damage Type</th>

<th>Percentage</th>

</tr>

"""

        if assessment:

            for key, value in assessment.damage.items():

                html += f"""

<tr>

<td>{key}</td>

<td>{value:.2f}%</td>

</tr>

"""

        html += """

</table>

</div>

"""

        # ======================================================
        # Recommendations
        # ======================================================

        html += """

<div class="section">

<h2>Recommendations</h2>

<ul>

"""

        if reasoning:

            for item in reasoning.recommendations:

                html += f"""

<li>{item}</li>

"""

        html += """

</ul>

</div>

"""
        # ======================================================
        # Notes
        # ======================================================

        if report.notes:

            html += """

<div class="section">

<h2>Notes</h2>

<ul>

"""

            for note in report.notes:

                html += f"""

<li>{note}</li>

"""

            html += """

</ul>

</div>

"""

        # ======================================================
        # Footer
        # ======================================================

        html += f"""

<hr>

<div class="footer">

<h3>GeoGuard AI Platform</h3>

<p>

AI-powered Disaster Intelligence & Assessment System

</p>

<p>

Organization :
<strong>{report.organization}</strong>

</p>

<p>

Analyst :
<strong>{report.analyst}</strong>

</p>

<p>

Version :
<strong>{report.version}</strong>

</p>

<p>

Generated :
<strong>{report.generated_at}</strong>

</p>

<p>

Report ID :
<strong>{report.report_id}</strong>

</p>

<p style="margin-top:30px;">

© 2026 GeoGuard AI Platform

</p>

</div>

"""

        # ======================================================
        # Close HTML
        # ======================================================

        html += """

</div>

</body>

</html>

"""

        return html