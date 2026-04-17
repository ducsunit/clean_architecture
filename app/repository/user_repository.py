from sqlalchemy.orm import Session

from app.domain.user import User


class UserRepository:
    def create_user(self, db: Session, name: str, email: str) -> User:
        user = User(name=name, email=email)
        db.add(user)
        db.commit()
        db.refresh(user)
        return user
    
    def get_all(self, db: Session) -> list[User]:
        return db.query(User).all()
    
    def get_by_id(self, db: Session, user_id: int) -> User | None:
        return db.query(User).filter(User.id==user_id).first()
    
    def delete_user(self, db: Session, user_id: int) -> User | None:
        user = db.query(User).filter(User.id==user_id).first()

        if user:
            db.delete(user)
            db.commit()
        return user