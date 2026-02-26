from sqlalchemy.orm import Session
from src.user.repository import UserRepository
from src.user.schemas import UserCreate, UserUpdate
from src.user.models import User
import hashlib

def hash_password(password: str) -> str:
    # A simple SHA-256 for demonstration. In production, use passlib with bcrypt or argon2.
    return hashlib.sha256(password.encode()).hexdigest()

class UserService:
    def __init__(self, db: Session):
        self.repo = UserRepository(db)

    def get_user(self, user_id: int) -> User | None:
        return self.repo.get_user_by_id(user_id)

    def get_users(self, skip: int = 0, limit: int = 100) -> list[User]:
        return self.repo.get_users(skip=skip, limit=limit)

    def create_user(self, user: UserCreate) -> User:
        if self.repo.get_user_by_email(user.email):
            raise ValueError("Email already registered")
        if self.repo.get_user_by_username(user.username):
            raise ValueError("Username already taken")

        hashed_password = hash_password(user.password)
        return self.repo.create_user(user, hashed_password)

    def update_user(self, user_id: int, user_update: UserUpdate) -> User | None:
        if user_update.email:
            existing = self.repo.get_user_by_email(user_update.email)
            if existing and existing.id != user_id:
                raise ValueError("Email already registered by another user")
                
        if user_update.username:
            existing = self.repo.get_user_by_username(user_update.username)
            if existing and existing.id != user_id:
                raise ValueError("Username already taken by another user")

        return self.repo.update_user(user_id, user_update)

    def delete_user(self, user_id: int) -> bool:
        return self.repo.delete_user(user_id)
