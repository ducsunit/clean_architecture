
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session


from app.core.database import get_db
from app.schema.user_schema import UserCreate, UserResponse
from app.service.user_service import UserService

router = APIRouter(prefix="/users", tags=["users"])

user_service = UserService()

@router.post("/", response_model=UserResponse, status_code=status.HTTP_201_CREATED)
def create_user(payload: UserCreate, db: Session = Depends(get_db)) -> UserResponse:
    user = user_service.create_user(db, payload.name, payload.email)
    return UserResponse.model_validate(user)

@router.get("/", response_model=list[UserResponse])
def get_users(db: Session = Depends(get_db)) -> list[UserResponse]:
    users =  user_service.get_users(db)
    return [UserResponse.model_validate(u) for u in users]

@router.get("/{user_id}", response_model=UserResponse)
def get_user(user_id: int, db: Session = Depends(get_db)) -> UserResponse:
    user =  user_service.get_user(db, user_id)

    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    
    return UserResponse.model_validate(user)

@router.delete("/{user_id}", response_model=UserResponse)
def delete_user(user_id: int, db: Session = Depends(get_db)) -> UserResponse:
    user = user_service.delete_user(db, user_id)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return UserResponse.model_validate(user)