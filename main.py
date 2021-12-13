import logging
import logging.config
import os
from fastapi import FastAPI
from fastapi.responses import JSONResponse
from fastapi import HTTPException
from infrastructure.routes import metrics_router
from exceptions.auth_error import AuthorizationException

logging_conf_path = os.path.join(os.path.dirname(__file__), "logging.ini")
logging.config.fileConfig(logging_conf_path, disable_existing_loggers=False)

app = FastAPI(title = "Ubademy - Metrics service",
            description = "Metrics service API")


@app.exception_handler(AuthorizationException)
async def auth_exception_handler(request, exc):
    error = {"message": exc.detail}
    logging.error(f"status_code: {exc.status_code} message: {exc.detail}")
    return JSONResponse(status_code = exc.status_code, content = error)


app.include_router(metrics_router.router, prefix='/metrics', tags=['metrics'])