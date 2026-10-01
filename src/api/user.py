from fastapi import APIRouter, Depends

from database.orm import User
from database.repository import ToDoRepository, UserRepository
from schema.reponse import UserSchema
from schema.request import SignUpRequest
from service.user import UserService

router = APIRouter()

@router.post("/sign-up",status_code = 201)
def user_sign_up_handler(
        request : SignUpRequest,
        user_service : UserService = Depends(),
        user_repo : UserRepository = Depends(),
) :
    # 1. requset body(username, password)
    # 2. password -> hashing -> hashed_password
    hashed_password : str = user_service.hash_password(
        plain_password=request.password
    )

    # 3. User(username, hashed_password)
    user:User = User.create(
        username = request.username, hashed_password = hashed_password
    )

    # 4. user -> db save
    user : User = user_repo.save_user(user=user)

    # 5. return user(id, username)
    return UserSchema.from_orm(user)

