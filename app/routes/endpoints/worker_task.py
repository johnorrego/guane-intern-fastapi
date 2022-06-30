from fastapi import APIRouter, BackgroundTasks, File, UploadFile
from worker.celery_app import celery_app
from os import getcwd

task_routes = APIRouter()


def celery_on_message(body):
    print(body)


def background_on_message(task):
    print(task.get(on_message=celery_on_message, propagate=False))


@task_routes.post("/{seconds}")
async def root(number: int, background_task: BackgroundTasks):
    task = celery_app.send_task(
        "worker.celery_worker.test_celery", args=[number])
    print(task, "--- This is the task code")
    background_task.add_task(background_on_message, task)
    return {"message": "Number received"}


@task_routes.post("/upload/file")
async def upload_file(background_task: BackgroundTasks, file: UploadFile = File(...)):
    with open(getcwd() + "/" + file.filename, "wb") as myfile:
        content = await file.read()
        myfile.write(content)
        myfile.close()
    task = celery_app.send_task(
        "worker.celery_worker.send_data", args=[file.filename])
    print(task, file.filename)
    background_task.add_task(background_on_message, task)
    return {"message": "File received"}


# @task_routes.post('/mensaje/{num}')
# def mensaje(num: str):
#     url = f"https://gttb.guane.dev/api/workers?task_complexity={num}"
#     objeto = requests.post(url)
#     print (objeto.json())
#     return objeto.json()
