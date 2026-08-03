"""
GeoGuard AI

Report API

Author: Shivam Salve
"""

import shutil
import tempfile
import traceback
from pathlib import Path

from fastapi import APIRouter
from fastapi import Depends
from fastapi import File
from fastapi import HTTPException
from fastapi import Request
from fastapi import UploadFile

from backend.api.dependencies import get_engine
from backend.api.schemas import (
    ReportFilesSchema,
    ReportResponse,
)
from backend.geoguard.engine import GeoGuardEngine
from backend.report.service import ReportService


router = APIRouter()


@router.post(

    "/report",

    response_model=ReportResponse,

    summary="Generate Professional Report",

    description="""
Generate professional disaster reports.

Outputs:

- HTML Report

- PDF Report

- Download Links
""",

)
async def generate_report(
    request: Request,
    image: UploadFile = File(...),
    engine: GeoGuardEngine = Depends(get_engine),
):
    """
    Generate a professional HTML and PDF disaster report.
    """

    # -----------------------------------------------------
    # Validate Upload
    # -----------------------------------------------------

    if image.filename is None:
        raise HTTPException(
            status_code=400,
            detail="No filename received.",
        )

    suffix = Path(image.filename).suffix.lower()

    allowed_extensions = {
        ".png",
        ".jpg",
        ".jpeg",
        ".tif",
        ".tiff",
    }

    if suffix not in allowed_extensions:
        raise HTTPException(
            status_code=400,
            detail=f"Unsupported image format: {suffix}",
        )

    # -----------------------------------------------------
    # Save Uploaded Image
    # -----------------------------------------------------

    with tempfile.NamedTemporaryFile(
        delete=False,
        suffix=suffix,
    ) as tmp:

        shutil.copyfileobj(image.file, tmp)

        temp_path = Path(tmp.name)

    try:

        # -------------------------------------------------
        # Run GeoGuard AI
        # -------------------------------------------------

        geoguard_result = engine.predict(
            damage_image=temp_path,
        )

        # -------------------------------------------------
        # Generate Report
        # -------------------------------------------------

        report_service = ReportService()

        report = report_service.generate(
            geoguard_result
        )

        # -------------------------------------------------
        # Build Download URLs
        # -------------------------------------------------

        base_url = str(request.base_url).rstrip("/")

        html_url = (
            f"{base_url}/api/download/"
            f"{Path(report.html_path).name}"
        )

        pdf_url = (
            f"{base_url}/api/download/"
            f"{Path(report.pdf_path).name}"
        )

        # -------------------------------------------------
        # Return Response
        # -------------------------------------------------

        return ReportResponse(

            success=True,

            message="Report generated successfully.",

            report=ReportFilesSchema(

                html_report=html_url,

                pdf_report=pdf_url,

            ),

        )

    except HTTPException:
        raise

    except Exception as e:

        traceback.print_exc()

        raise HTTPException(
            status_code=500,
            detail=str(e),
        )

    finally:

        if temp_path.exists():
            temp_path.unlink()