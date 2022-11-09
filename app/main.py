from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from .config import settings
from .routers import repos
app = FastAPI(
    docs_url=f"{settings.SERVICE_ENDPOINT}",
    openapi_url=f"{settings.SERVICE_ENDPOINT}/openapi.json",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(repos.router, prefix=f"{settings.SERVICE_ENDPOINT}/repos")
