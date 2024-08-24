from fastapi import Query, HTTPException, Request, Depends
from fastapi.responses import JSONResponse
from pydantic import BaseModel, Field
from BBDD.database import Session
from models.servicios import Service as ModelService
from fastapi.encoders import jsonable_encoder
from fastapi import APIRouter
from fastapi.security import HTTPBearer
from admin_jwt import validateToken

routersService = APIRouter()


class Service(BaseModel):
    id: int
    titulo: str = Field(default='Nombre del Servicio', min_length=3, max_length=20)
    categoria: str = Field(default='Nombre de la Categoría del Servicio', min_length=8, max_length=50)
    descripcion: str = Field(min_length=10, max_length=150)
    precio: float = Field(default='Aca va el precio en pesos Argentinos')
 

class BearerJWT(HTTPBearer):
    async def __call__(self, request: Request):
        auth = await super().__call__(request)
        data = validateToken(auth.credentials)
        if data['email'] != 'aestheticestetica22@gmail.com':
            raise HTTPException(status_code=403, detail='Credenciales incorrectas')



@routersService.get('/Servicios', tags=['Servicios'], dependencies=[Depends(BearerJWT())])
def get_servicios():
    ddbb = Session()
    data = ddbb.query(ModelService).all()
    return JSONResponse(content=jsonable_encoder(data))

@routersService.get('/Servicios/{id}',tags=['Servicios'])
def get_servicio(id: int):
    ddbb = Session()
    data = ddbb.query(ModelService).filter(ModelService.id == id).first()
    if not data:
        return JSONResponse(status_code=404, content={'message': 'Recurso no encontrado'})
    return JSONResponse(status_code=200, content=jsonable_encoder(data))
    
    
@routersService.get('/Servicios/', tags=['Servicios'])
def get_servicios_by_category(categoria: str = Query(min_length=8, max_length=50)):
    ddbb = Session()
    data = ddbb.query(ModelService).filter(ModelService.categoria == categoria).all()
    if not data:
        return JSONResponse(status_code=404, content={'message': 'No se encontraron recursos en esa categoria'})
    return JSONResponse(status_code=200, content=jsonable_encoder(data))
    


@routersService.post('/Servicios', tags=['Servicios'])
def create_servicio(servicio: Service):
    ddbb = Session()
    newServicio = ModelService(**servicio.dict())
    ddbb.add(newServicio)
    ddbb.commit()
    return JSONResponse(status_code=201, content={'message': 'Se ha cargado un nuevo Servicio'})


@routersService.put('/Servicios/{id}', tags=['Servicios'])
def update_servicio(id: int, servicio: Service):
    ddbb = Session()
    data = ddbb.query(ModelService).filter(ModelService.id == id).first()
    if not data:
        return JSONResponse(status_code=404, content={'message': 'No se encontro el Recurso'})
    data.titulo = servicio.titulo
    data.categoria = servicio.categoria
    data.descripcion = servicio.descripcion
    data.precio = servicio.precio
    ddbb.commit()
    return JSONResponse(content={'message': 'Contenido modificado exitosamente'})
    
    
@routersService.delete('/Servicios/{id}', tags=['Servicios'])
def delete_servicio(id: int):
    ddbb = Session()
    data = ddbb.query(ModelService).filter(ModelService.id == id).first()
    if not data:
        return JSONResponse(status_code=404, content={'message': 'No se encontro el Recurso'})
    ddbb.delete(data)
    ddbb.commit()
    return JSONResponse(content={'message': 'El servicio ha sido eliminado', 'data': jsonable_encoder(data)})

