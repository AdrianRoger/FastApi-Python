from sqlalchemy.orm import Session

from crud_fastapi.src.models.user_model import User
from crud_fastapi.src.schemas.user_schemas import UserCreate, UserUpdate


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


def get_user_by_id(db: Session, id: int):
    return db.query(User).filter(User.id == id).first()


def get_all_users(db: Session, skip: int = 0, limit: int = 10):
    return db.query(User).offset(skip).limit(limit).all()


def update_user(db: Session, id: int, user: UserUpdate):
    existing_user = db.query(User).filter(User.id == id).first()
    if not existing_user:
        return None

    # update fields
    existing_user.username = user.username
    existing_user.email = user.email
    existing_user.password = user.password  # Lembrar de adicionar hash posteriormente

    db.commit()
    db.refresh(existing_user)
    return existing_user
