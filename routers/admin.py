from fastapi import APIRouter
from pydantic import BaseModel, Field
from admin_jwt import createToken
from fastapi.responses import JSONResponse

routersLogin = APIRouter()

class Admin(BaseModel):
    email: str = Field(default='Mail de administrador', min_length=12, max_length=35)
    password: str = Field(default='Contraseña', min_length=3, max_length=30)



@routersLogin.post('/Login', tags=['Autenticacion'])
def autenticar_login(admin: Admin):
    if admin.email == 'aestheticestetica22@gmail.com' and admin.password == 'esteticaaesthetic2024': 
        token: str = createToken(admin.dict())
        print(token)
        return JSONResponse(content= token)

