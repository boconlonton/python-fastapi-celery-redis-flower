from fastapi import FastAPI

from api.task import tasks_api

app = FastAPI()
app.include_router(tasks_api, prefix='/tasks', tags=['tasks'])
