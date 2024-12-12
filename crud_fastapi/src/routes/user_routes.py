from http import HTTPStatus

from fastapi import APIRouter, Depends, HTTPException
from pydantic import EmailStr
from sqlalchemy.orm import Session

from crud_fastapi.src.controllers.user_controller import (
    create_user_controller,
    get_user_by_email_controller,
)
from crud_fastapi.src.database.connection import get_db
from crud_fastapi.src.schemas.user_schemas import UserCreate, UserResponse

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
