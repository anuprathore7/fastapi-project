from fastapi import APIRouter 

router = APIRouter(
    tags=["home"],
)


@router.get("/", summary="Home route")
def home_route():
    return {"message": "This is home route"}