"""
GeoGuard AI

Global Exception Handlers

Author: Shivam Salve
"""

from fastapi import Request
from fastapi import HTTPException
from fastapi.responses import JSONResponse
from fastapi.exceptions import RequestValidationError


async def http_exception_handler(
    request: Request,
    exc: HTTPException,
):

    return JSONResponse(

        status_code=exc.status_code,

        content={

            "success": False,

            "error": "HTTP Exception",

            "message": exc.detail,

            "path": str(request.url.path),

        },

    )


async def validation_exception_handler(
    request: Request,
    exc: RequestValidationError,
):

    return JSONResponse(

        status_code=422,

        content={

            "success": False,

            "error": "Validation Error",

            "message": "Invalid request.",

            "details": exc.errors(),

            "path": str(request.url.path),

        },

    )


async def global_exception_handler(
    request: Request,
    exc: Exception,
):

    return JSONResponse(

        status_code=500,

        content={

            "success": False,

            "error": "Internal Server Error",

            "message": "Unexpected server error.",

            "path": str(request.url.path),

        },

    )