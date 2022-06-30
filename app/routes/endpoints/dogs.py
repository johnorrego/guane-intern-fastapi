
from typing import List
from schemas.dog import Dog_Pydantic, DogIn_Pydantic, Dog
from schemas.user import User_Pydantic, User
from security.security import get_current_user
from fastapi import APIRouter, HTTPException, Depends
from urllib.request import urlopen
import json

dog_routes = APIRouter()


@dog_routes.get("/", response_model=List[Dog_Pydantic])
async def get_dogs():
    return await Dog_Pydantic.from_queryset(Dog.all())


@dog_routes.get("/{name}/", response_model=Dog_Pydantic)
async def get_dog_by_name(dog_name: str):
    return await Dog_Pydantic.from_queryset_single(Dog.get(name=dog_name))


@dog_routes.get("/is_adopted")
async def get_dogs_by_adoption():
    return await Dog_Pydantic.from_queryset(Dog.filter(is_adopted=True))


@dog_routes.post("/user_id/{id_usr}", response_model=Dog_Pydantic)
async def create_dog(id_usr: int, dog: DogIn_Pydantic, user: User_Pydantic = Depends(get_current_user)):
    imagen_url = 'https://dog.ceo/api/breeds/image/random'
    response = urlopen(imagen_url)
    img = json.loads(response.read())
    if img["status"] == 'success':
        usr = await User.get(id_user=id_usr)
        dog_obj = Dog(name=dog.name, picture=img["message"],
                      is_adopted=dog.is_adopted, user_id=usr)
    await dog_obj.save()

    return await Dog_Pydantic.from_tortoise_orm(dog_obj)


@dog_routes.put("/id_dog/{dog_id}", response_model=Dog_Pydantic)
async def update_dog(dog_id: int, dog: DogIn_Pydantic):
    imagen_url = 'https://dog.ceo/api/breeds/image/random'
    response = urlopen(imagen_url)
    img = json.loads(response.read())
    if img["status"] == 'success':
        await Dog.filter(id_dog=dog_id).update(name=dog.name,
                                               picture=img["message"],
                                               is_adopted=dog.is_adopted)

        return await Dog_Pydantic.from_queryset_single(Dog.get(id_dog=dog_id))


@dog_routes.delete("/{id_dog}")
async def delete_dog(dog_id: int):
    res = await Dog.filter(id_dog=dog_id).delete()
    if res:
        return HTTPException(status_code=200, detail=f"Dog {dog_id} deleted", headers="Success")
    else:
        return HTTPException(status_code=404, detail="Not found data", headers="Not found error")
