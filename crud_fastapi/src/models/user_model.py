from sqlalchemy import Column, Integer, String

from crud_fastapi.src.database.connection import Base


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True)  # ID único
    username = Column(String, index=True)  # Nome do usuário
    email = Column(String, unique=True, index=True)  # Email único
    password = Column(String)  # Senha do usuário (não será retornada na API)
