from http import HTTPStatus

from fastapi import APIRouter, Depends, HTTPException
from pydantic import EmailStr
from sqlalchemy.orm import Session

from crud_fastapi.src.controllers.user_controller import (
    create_user_controller,
    get_all_users_controller,
    get_user_by_email_controller,
    get_user_by_id_controller,
    update_user_controller,
)
from crud_fastapi.src.database.connection import get_db
from crud_fastapi.src.schemas.user_schemas import UserCreate, UserResponse, UserUpdate
from crud_fastapi.src.services.user_service import ConflictError

router = APIRouter()


@router.post('/', response_model=UserResponse, status_code=HTTPStatus.CREATED)
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    try:
        return create_user_controller(db, user)
    except ValueError as e:
        raise HTTPException(status_code=HTTPStatus.CONFLICT, detail=str(e))


@router.get('/email/{email}', response_model=UserResponse, status_code=HTTPStatus.OK)
def get_user_by_email(email: EmailStr, db: Session = Depends(get_db)):
    try:
        return get_user_by_email_controller(db, email)
    except ValueError as e:
        raise HTTPException(status_code=HTTPStatus.NOT_FOUND, detail=str(e))


@router.get('/{id}', response_model=UserResponse, status_code=HTTPStatus.OK)
def get_user_by_id(id: int, db: Session = Depends(get_db)):
    try:
        return get_user_by_id_controller(db, id)
    except ValueError as e:
        raise HTTPException(status_code=HTTPStatus.NOT_FOUND, detail=str(e))


@router.get('/')
def get_all_users(page: int = 1, limit: int = 10, db: Session = Depends(get_db)):
    try:
        users = get_all_users_controller(db, page=page, limit=limit)
        if not users:
            raise HTTPException(
                status_code=HTTPStatus.NOT_FOUND, detail='No users found for the specified page.'
            )
        return users
    except ValueError as e:
        raise HTTPException(status_code=HTTPStatus.BAD_REQUEST, detail=str(e))


@router.put('/{id}')
def update_user(id: int, user: UserUpdate, db: Session = Depends(get_db)):
    try:
        user_updated = update_user_controller(db, id, user)
        return user_updated
    except ValueError as e:
        raise HTTPException(status_code=HTTPStatus.NOT_FOUND, detail=str(e))
    except ConflictError as e:
        raise HTTPException(status_code=HTTPStatus.CONFLICT, detail=str(e))
