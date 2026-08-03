"""
GeoGuard AI

FastAPI Application

Author: Shivam Salve
"""
from fastapi.middleware.cors import CORSMiddleware

from fastapi import FastAPI

from backend.api.tags import tags_metadata

from backend.api.config import settings

from backend.api.routers.health import router as health_router

from backend.api.routers.prediction import (
    router as prediction_router,
)

from backend.api.routers.report import (
    router as report_router,
)

from backend.api.routers.download import (
    router as download_router,
)

from fastapi import HTTPException
from fastapi.exceptions import RequestValidationError

from backend.api.exceptions import (
    global_exception_handler,
    http_exception_handler,
    validation_exception_handler,
)


app = FastAPI(

    title="GeoGuard AI",

    summary=(
        "AI-powered disaster damage assessment platform "
        "using satellite imagery and Large Language Models."
    ),

    description="""
# GeoGuard AI

GeoGuard AI is an end-to-end disaster assessment platform.

## Features

- Land Cover Analysis
- Flood Detection
- Building Damage Assessment
- AI Disaster Reasoning (Gemma 2)
- Professional HTML Reports
- Professional PDF Reports
- Download API

## AI Models

- SegFormer
- Gemma 2
- PyTorch

## Developed By

Shivam Salve
""",

    version="1.0.0",

    contact={
        "name": "Shivam Salve",
        "email": "shivam@example.com",
    },

    license_info={
        "name": "MIT License",
    },
    docs_url="/docs",

    redoc_url="/redoc",

    openapi_url="/openapi.json",

    openapi_tags=tags_metadata,

)

# ==========================================================
# CORS
# ==========================================================

# ==========================================================
# CORS
# ==========================================================

app.add_middleware(
    CORSMiddleware,

    allow_origins=[
        # Vite Development
        "http://localhost:5173",
        "http://127.0.0.1:5173",

        # Vite Preview / Production
        "http://localhost:4173",
        "http://127.0.0.1:4173",

        # Local Network (update IP if needed)
        "http://192.168.0.184:4173",
    ],

    allow_credentials=True,

    allow_methods=["*"],

    allow_headers=["*"],
)


app.add_exception_handler(
    HTTPException,
    http_exception_handler,
)

app.add_exception_handler(
    RequestValidationError,
    validation_exception_handler,
)

app.add_exception_handler(
    Exception,
    global_exception_handler,
)


app.include_router(

    prediction_router,

    prefix=settings.API_PREFIX,

    tags=["Prediction"],

)

app.include_router(

    download_router,

    prefix=settings.API_PREFIX,

    tags=["Download"],

)


app.include_router(

    report_router,

    prefix=settings.API_PREFIX,

    tags=["Report"],

)


app.include_router(

    health_router,

    prefix=settings.API_PREFIX,

    tags=["Health"],

)


@app.get("/")

def root():

    return {

        "project": settings.PROJECT_NAME,

        "version": settings.VERSION,

        "status": "running",

    }