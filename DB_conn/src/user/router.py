from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from src.utils.db import get_db
from src.user.schemas import User, UserCreate, UserUpdate
from src.user.service import UserService

router = APIRouter(
    prefix="/users",
    tags=["Users"]
)

def get_user_service(db: Session = Depends(get_db)):
    return UserService(db)

@router.post("/", response_model=User, status_code=status.HTTP_201_CREATED)
def create_user(user: UserCreate, service: UserService = Depends(get_user_service)):
    try:
        return service.create_user(user)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.get("/", response_model=list[User])
def read_users(skip: int = 0, limit: int = 100, service: UserService = Depends(get_user_service)):
    return service.get_users(skip=skip, limit=limit)

@router.get("/{user_id}", response_model=User)
def read_user(user_id: int, service: UserService = Depends(get_user_service)):
    user = service.get_user(user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@router.patch("/{user_id}", response_model=User)
def update_user(user_id: int, user_update: UserUpdate, service: UserService = Depends(get_user_service)):
    try:
        user = service.update_user(user_id, user_update)
        if not user:
            raise HTTPException(status_code=404, detail="User not found")
        return user
    except ValueError as e:
         raise HTTPException(status_code=400, detail=str(e))

@router.delete("/{user_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_user(user_id: int, service: UserService = Depends(get_user_service)):
    if not service.delete_user(user_id):
        raise HTTPException(status_code=404, detail="User not found")
    return None
