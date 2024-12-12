from sqlalchemy.orm import Session

from crud_fastapi.src.schemas.user_schemas import UserCreate, UserUpdate
from crud_fastapi.src.services.user_service import (
    create_user_service,
    delete_user_by_id_service,
    get_all_users_service,
    get_user_by_email_service,
    get_user_by_id_service,
    update_user_service,
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


def get_user_by_id_controller(db: Session, id: int):
    try:
        return get_user_by_id_service(db, id)
    except ValueError as e:
        raise e


def get_all_users_controller(db: Session, page: int = 1, limit: int = 10):
    try:
        return get_all_users_service(db, page, limit)
    except ValueError as e:
        raise e


def update_user_controller(db: Session, id: int, user: UserUpdate):
    try:
        return update_user_service(db, id, user)
    except ValueError as e:
        raise e
    

def delete_user_by_id_controller(db: Session, id: int):
    try:
        delete_user_by_id_service(db, id)
        return {'message': 'User deleted successfully.'}
    except ValueError as e:
        raise e
