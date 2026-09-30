from fastapi import APIRouter



router = APIRouter()

@router.post("/sign-up")
def user_sign_up_handler() :
    return True

