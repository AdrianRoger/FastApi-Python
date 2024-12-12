from sqlalchemy.orm import Session

from crud_fastapi.src.schemas.user_schemas import UserCreate
from crud_fastapi.src.services.user_service import (
    create_user_service,
    get_user_by_email_service,
)


def create_user_controller(db: Session, user: UserCreate):
    try:
        return create_user_service(db, user)
    except ValueError as e:
        raise e


def get_user_by_email_controller(db: Session, email: str):
    try:
        return get_user_by_email_service(db, email)
    except ValueError as e:
        raise e