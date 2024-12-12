from sqlalchemy.orm import Session

from crud_fastapi.src.repositories.user_repository import (
    create_user,
    get_all_users,
    get_user_by_email,
    get_user_by_id,
)
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


def get_user_by_id_service(db: Session, id: int):
    user = get_user_by_id(db, id)
    if not user:
        raise ValueError('User not found.')
    return user


def get_all_users_service(db: Session, page: int = 1, limit: int = 10):
    if page < 1:
        raise ValueError('Page must be 1 or greater.')

    return get_all_users(db, (page - 1) * limit, limit)
