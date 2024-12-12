from fastapi import FastAPI

from .src.database.connection import Base, engine
from .src.routes.user_routes import router as user_router

Base.metadata.create_all(bind=engine)

app = FastAPI()


app.include_router(user_router, prefix='/users', tags=['Users'])
