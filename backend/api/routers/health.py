"""
GeoGuard AI

Health Endpoint

Author: Shivam Salve
"""

from fastapi import APIRouter


router = APIRouter()


@router.get("/health")

def health():

    return {

        "status": "healthy",

        "service": "GeoGuard AI",

    }