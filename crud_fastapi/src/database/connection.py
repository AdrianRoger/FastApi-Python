from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Base para os modelos
Base = declarative_base()

# Configuração do banco de dados
DATABASE_URL = 'sqlite:///./crud_fastapi.db'

# Engine do SQLAlchemy
engine = create_engine(DATABASE_URL, echo=True, connect_args={'check_same_thread': False})

# Sessão do banco
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
