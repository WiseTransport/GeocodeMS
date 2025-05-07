import os
from typing import Any
import googlemaps
from fastapi import APIRouter, Query

GOOGLE_KEY = os.environ["GOOGLE_KEY"]

router = APIRouter(prefix="/geocode")
gmaps = googlemaps.Client(key=GOOGLE_KEY)


@router.get("/")
async def geocode(address: str = Query()) -> Any:
    return gmaps.geocode(address)
