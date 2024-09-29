from fastapi import APIRouter, Request

router = APIRouter()

@router.get("/common")
def common_route():
    return {"message": "This is a common route"}