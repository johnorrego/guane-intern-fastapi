
# from dotenv import load_dotenv
from fastapi import FastAPI
from routes.auth import auth_routes
from database.db import db_connection
from fastapi.middleware.cors import CORSMiddleware  # adding cors headers


app = FastAPI()

# Run db connection
@app.on_event("startup")
async def startup():
    return db_connection(app)


@app.on_event("shutdown")
async def shutdown():
    return 'Closing'

# Run endpoints
app.include_router(auth_routes, prefix="/api")

# Para cargar la variable de entorno
# load_dotenv()


# Función que permite el intercambio de recursos de origen cruzado
# Le permite compartir recursos entre diferentes aplicaciones
# que no se ejecutan en el mismo servidor.
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
