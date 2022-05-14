import time

from celery import Task

from backend.worker.app_worker import app

@app.task(name="create_task")
def create_task(task_type):
    time.sleep(int(task_type) * 10)
    return True
