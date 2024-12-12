from sqlalchemy.orm import Session

from crud_fastapi.src.repositories.user_repository import create_user, get_user_by_email
from crud_fastapi.src.schemas.user_schemas import UserCreate


def create_user_service(db: Session, user: UserCreate):
    existing_user = get_user_by_email(db, user.email)
    if existing_user:
        raise ValueError('Email already in use.')
    return create_user(db, user)


def get_user_by_email_service(db: Session, email: str):
    user = get_user_by_email(db, email)
    if not user:
        raise ValueError('User not found.')
    return user
