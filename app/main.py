import logging
import os
from .api import endpoints
from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI

def _configure_logging() -> None:
    # Default to INFO to avoid noisy third-party DEBUG logs
    level_name = os.getenv("LOG_LEVEL", "debug").upper()
    level = getattr(logging, level_name, logging.INFO)
    logging.basicConfig(level=level, format='%(asctime)s %(levelname)s [%(name)s] %(message)s')
    # Silence noisy libraries
    for noisy in [
        "openai",
        "httpx",
        "urllib3",
        # "pinecone",
        "langchain",
        "langchain_openai",
        "sqlalchemy.engine",
        "botocore",
        "boto3",
    ]:
        logging.getLogger(noisy).setLevel(logging.WARNING)


_configure_logging()
logger = logging.getLogger(__name__)

app = FastAPI(title="Ecommerce ERP AI Agent")
# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # TODO: Add custom origins
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.include_router(endpoints.router)


@app.get("/")
async def root():
    logger.debug("Root endpoint hit")
    return {"message": "Welcome to the Ecommerce ERP AI Agent!"}