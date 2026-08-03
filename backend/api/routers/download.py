"""
GeoGuard AI

Download API

Author: Shivam Salve
"""

from pathlib import Path

from fastapi import APIRouter
from fastapi import HTTPException
from fastapi.responses import FileResponse

from backend.api.config import settings

router = APIRouter()

REPORT_DIR = settings.REPORT_DIR

DAMAGE_DIR = Path("backend/outputs/damage")


@router.get(
    "/download/{filename}",
    summary="Download Generated File",
    description="""
Download generated reports or AI prediction images.
""",
)
def download_file(filename: str):

    report_file = REPORT_DIR / filename
    damage_file = DAMAGE_DIR / filename

    if report_file.exists():
        file_path = report_file

    elif damage_file.exists():
        file_path = damage_file

    else:
        raise HTTPException(
            status_code=404,
            detail="File not found.",
        )

    return FileResponse(
        path=file_path,
        filename=file_path.name,
        media_type="application/octet-stream",
    )