import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import Session, sessionmaker
from sqlalchemy.pool import StaticPool

from crud_fastapi.main import app
from crud_fastapi.src.database.connection import Base, get_db
from crud_fastapi.src.models.user_model import User

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


# Created user fixture
@pytest.fixture
def db_with_single_user(test_db: Session):
    user_data = {
        'username': 'teste user',
        'email': 'teste_user@example.com',
        'password': 'securepassword',
    }

    user = User(**user_data)
    test_db.add(user)
    test_db.commit()

    return user, test_db
