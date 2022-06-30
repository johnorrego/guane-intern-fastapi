
from fastapi import APIRouter
from routes.endpoints import users, dogs, login

auth_routes = APIRouter()
auth_routes.include_router(users.usr_routes, prefix="/users", tags=["users"])
auth_routes.include_router(dogs.dog_routes, prefix="/dogs", tags=["dogs"])
auth_routes.include_router(login.login_routes, prefix="/login", tags=["login"])
