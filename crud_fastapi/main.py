from fastapi import FastAPI

from crud_fastapi.src.database.connection import Base, engine
from crud_fastapi.src.routes.user_routes import router as user_router

Base.metadata.create_all(bind=engine)

app = FastAPI()


app.include_router(user_router, prefix='/users', tags=['Users'])
