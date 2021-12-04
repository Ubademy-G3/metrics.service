from fastapi import FastAPI
from fastapi.responses import JSONResponse
from fastapi import HTTPException
from infrastructure.routes import metrics_router

app = FastAPI(title = "Ubademy - Metrics service",
            description = "Metrics service API")

app.include_router(metrics_router.router, prefix='/metrics', tags=['metrics'])