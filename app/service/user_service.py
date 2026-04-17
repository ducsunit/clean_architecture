from sqlalchemy.orm import Session
from app.domain.user import User
from app.repository.user_repository import UserRepository


class UserService:
    def __init__(self) -> None:
        self.repo: UserRepository = UserRepository()
    
    def create_user(self, db: Session, name: str, email: str) -> User:
        return self.repo.create_user(db, name, email)
    
    def get_users(self, db: Session) -> list[User]:
        return self.repo.get_all(db)
    
    def get_user(self, db: Session, user_id: int) -> User | None:
        return self.repo.get_by_id(db, user_id)
    
    def delete_user(self, db: Session, user_id: int) -> User | None:
        return self.repo.delete_user(db, user_id)

        