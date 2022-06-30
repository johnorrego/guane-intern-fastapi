## guane-intern-fastapi
API Rest

## La siguiente API fue desarrollado utilizando Python con el framework FastAPI, Celery, Redis, Rabbitmq, PostgresSLQ, Tortoise ORM y Docker.


## Intro
Se realizó una api que sigue los principios REST con un componente arquitectónico adicional que incluye realizar un llamado a una tarea asíncrona.
La api maneja 2 entidades: Dog, User.


## Instalación
- Se debe ejecutar el archivo "docker-compose.yml", este se encargará de crear las imagenes necesarias y posteriormente sus contenedores.


## Endpoints
Se definierón las siguientes rutas:
Dogs
- http://localhost:8002/api/dogs --> get : obtener todos los dogs
- http://localhost:8002/api/dogs/{name} --> get : obtener los dogs por nombre
- http://localhost:8002/api/dogs/is_adopted --> get : obtener todos los dogs adoptados
- http://localhost:8002/api/dogs/user_id/{id_usr} --> post : crear un dog (requiere de autorización mediante un token)
- http://localhost:8002/api/dogs/id_dog/{dog_id} --> put : actualizar un dog por nombre
- http://localhost:8002/api/dogs/{id_dog} --> delete : eliminar un dog por nombre

Login
- http://localhost:8002/api/login/token --> post : Se envía el username y el password del user y nos devuelve un token.

Users
- http://localhost:8002/api/users --> get : obtener todos los users
- http://localhost:8002/api/users/{id_user} --> get : obtener un user por id
- http://localhost:8002/api/users --> post : crear un user
- http://localhost:8002/api/users/{id_user} --> put : actualizar un user por id
- http://localhost:8002/api/users/{id_user} --> delete : eliminar un user por id

Worker_Task
- http://localhost:8002/api/tasks/{seconds} --> post : enviamos un valor númerico para activar la tarea.
- http://localhost:8002/api/tasks/upload/file --> post : permite enviar un documento a otra api en segundo plano.







