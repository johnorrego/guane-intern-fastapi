
from tortoise import Tortoise
from tortoise.contrib.fastapi import register_tortoise


Tortoise.init_models(["models"], 'models')


# Configuración y generación de la BD
def db_connection(app):
    register_tortoise(
        app,
        db_url="postgres://postgres:postgres@db:5432/sistema_adopcion",
        modules={"models": ["models"]},
        generate_schemas=True,
        add_exception_handlers=True
    )
