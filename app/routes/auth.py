
from fastapi import APIRouter
from routes.endpoints import users, dogs, login, worker_task

auth_routes = APIRouter()
auth_routes.include_router(users.usr_routes, prefix="/users", tags=["User"])
auth_routes.include_router(dogs.dog_routes, prefix="/dogs", tags=["Dog"])
auth_routes.include_router(login.login_routes, prefix="/login", tags=["Login"])
auth_routes.include_router(worker_task.task_routes, prefix="/task", tags=["Task"])