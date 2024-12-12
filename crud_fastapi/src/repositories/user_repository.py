from sqlalchemy.orm import Session

from crud_fastapi.src.models.user_model import User
from crud_fastapi.src.schemas.user_schemas import UserCreate


def create_user(db: Session, user: UserCreate):
    new_user = User(
        username=user.username,
        email=user.email,
        password=user.password,  # Lembrar de adicionar hash posteriormente
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


def get_user_by_email(db: Session, email: str):
    return db.query(User).filter(User.email == email).first()
