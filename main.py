from fastapi import FastAPI
from fastapi.responses import JSONResponse
from fastapi import HTTPException
from infrastructure.routes import metrics_router
from exceptions.auth_error import AuthorizationException

app = FastAPI(title = "Ubademy - Metrics service",
            description = "Metrics service API")


@app.exception_handler(AuthorizationException)
async def auth_exception_handler(request, exc):
    error = {"message": exc.detail}
    return JSONResponse(status_code = exc.status_code, content = error)


app.include_router(metrics_router.router, prefix='/metrics', tags=['metrics'])