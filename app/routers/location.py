from fastapi import APIRouter, Depends, Form
from fastapi.responses import JSONResponse
from app.services.service_location import LocationService

router = APIRouter(
    prefix="/location",
    tags=["LOCATION"],
    responses={404: {"message": "Not found"}}
)

location_service = LocationService()

@router.get("/province")
async def get_all():
    return location_service.province()

@router.get("/country")
async def get_all():
    return location_service.country()

@router.get("/country/search")
async def get_all():
    return location_service.country()