from celery import current_task
from fastapi.responses import FileResponse
from .celery_app import celery_app
from os import getcwd
from time import sleep
import requests


@celery_app.task(acks_late=True)
def test_celery(number: int) -> int:
    for i in range(1, 11):
        sleep(1)
        current_task.update_state(state='PROGRESS',
                                  meta={'process_percent': i*10})
    url = f"https://gttb.guane.dev/api/workers?task_complexity={number}"
    objeto = requests.post(url)
    return f"test task return {objeto.json()}"


@celery_app.task(acks_late=True)
def send_data(file_name: str) -> str:
    sleep(3)
    data = FileResponse(getcwd() + "/" + file_name)
    url = f"https://gttb.guane.dev/api/files"
    obj = requests.post(url, data)
    return f"test task return {obj}"
