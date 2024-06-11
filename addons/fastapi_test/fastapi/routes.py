from fastapi import APIRouter
from fastapi.responses import JSONResponse
from .jeans_data import jeans_data

router = APIRouter()

@router.get("/jeans", response_class=JSONResponse)
def get_product_data():
    return jeans_data
