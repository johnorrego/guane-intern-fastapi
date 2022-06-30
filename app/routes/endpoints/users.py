
from typing import List
from schemas.user import User_Pydantic, UserIn_Pydantic, User
from fastapi import APIRouter, HTTPException
from security.security import get_password_hash

usr_routes = APIRouter()

@usr_routes.get("/", response_model=List[User_Pydantic])
async def get_users():
    return await User_Pydantic.from_queryset(User.all())

# @usr_routes.get("/{name}", response_model=User_Pydantic)
# async def get_usr_by_name(usr_name: str):
#     return await User_Pydantic.from_queryset_single(User.get(name=usr_name))

@usr_routes.get("/{id_user}", response_model=User_Pydantic)
async def get_usr_by_id(usr_id: int):
    return await User_Pydantic.from_queryset_single(User.get(id_user=usr_id))

@usr_routes.post("/", response_model=User_Pydantic)
async def create_user(user: UserIn_Pydantic):
    user_obj = User(name=user.name, last_name=user.last_name,
                    email=user.email, username=user.username,
                    hashed_password=get_password_hash(user.hashed_password))
    await user_obj.save()

    return await User_Pydantic.from_tortoise_orm(user_obj)

@usr_routes.put("/{id_user}", response_model=User_Pydantic)
async def update_user(usr_id: int, user: UserIn_Pydantic):
    await User.filter(id_user=usr_id).update(name=user.name, last_name=user.last_name,
                                             email=user.email, username=user.username, 
                                             hashed_password=get_password_hash(user.hashed_password))
    return await User_Pydantic.from_queryset_single(User.get(id_user=usr_id))

@usr_routes.delete("/{id_user}")
async def delete_user(usr_id: int):
    res = await User.filter(id_user=usr_id).delete()
    if res:
        return HTTPException(status_code=200, detail=f"User {usr_id} deleted")
    else:
        return HTTPException(status_code=404, detail="Not Found Data")
