from http import HTTPStatus

from fastapi import FastAPI

app = FastAPI()


@app.get('/hello-world', status_code=HTTPStatus.OK)
def hello_world():
    return {'message': 'hello world'}
