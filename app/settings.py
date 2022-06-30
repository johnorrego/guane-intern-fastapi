
DATABASE_CONFIG = {
    "connections": {
        "default": "postgres://postgres:postgres@db:5432/sistema_adopcion"
    },
    "apps": {
        "models": {
            "models": ["models"],
            "default_connection": "default",
        },
    },
}
