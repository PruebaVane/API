from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from BBDD.database import engine, Base
from routers.servicio import routersService
from routers.admin import routersLogin


app = FastAPI(
    title='Api Servicios', 
    description='Aca se encuentra el CRUD de servicios de Aesthetic', 
    version='0.0.1')

    
app.include_router(routersService)
app.include_router(routersLogin)

Base.metadata.create_all(bind=engine)


@app.get('/', tags=['Inicio'])
def index():
    return HTMLResponse('<h1> Activa la Carga de Servicios de ASETHETIC </h1>')


