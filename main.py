from pathlib import Path

from ms_core.setup import include_routers
import uvicorn as uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

application = FastAPI(
    title="GeocodeMS",
)


application.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

include_routers(application, Path("app") / "routers")
