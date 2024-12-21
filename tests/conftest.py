from typing import List

import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import Session, sessionmaker
from sqlalchemy.pool import StaticPool

from crud_fastapi.main import app
from crud_fastapi.src.database.connection import Base, get_db
from crud_fastapi.src.models.user_model import User
from crud_fastapi.src.schemas.user_schemas import UserCreate
from tests.fixtures.data import USERS_FIXTURE_1, USERS_FIXTURE_2, USERS_FIXTURE_LARGE

TEST_DATABASE_URL = 'sqlite:///:memory:'

engine = create_engine(
    TEST_DATABASE_URL,
    connect_args={'check_same_thread': False},
    poolclass=StaticPool,
)
TestingSessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine,
)


# Fixture to provide a clean database session
@pytest.fixture
def test_db():
    def override_get_db():
        db_session = TestingSessionLocal()
        try:
            yield db_session
        finally:
            db_session.close()

    app.dependency_overrides[get_db] = override_get_db

    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)

    yield TestingSessionLocal()

    Base.metadata.drop_all(bind=engine)


@pytest.fixture
def test_client(test_db):
    with TestClient(app) as client:
        yield client


# Axiliary Function
def seed_users(db: Session, users_data: List[UserCreate]):
    """Helper function to seed users"""
    for user_data in users_data:
        db_user = User(**user_data.model_dump())
        db.add(db_user)
    db.commit()


# Create Fixture for each data case
@pytest.fixture
def db_with_users_1(test_db: Session):
    """Fixture with first set of users"""
    seed_users(test_db, USERS_FIXTURE_1)
    return test_db


@pytest.fixture
def db_with_users_2(test_db: Session):
    """Fixture with second set of users"""
    seed_users(test_db, USERS_FIXTURE_2)
    return test_db


@pytest.fixture
def db_empty(test_db: Session):
    """Fixture with no users"""
    return test_db


@pytest.fixture
def db_with_many_users(test_db: Session):
    """Fixture with many users"""
    seed_users(test_db, USERS_FIXTURE_LARGE)
    return test_db
