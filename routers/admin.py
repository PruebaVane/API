from fastapi import APIRouter
from pydantic import BaseModel, Field
from jwt_utils import createToken
from fastapi.responses import JSONResponse

routersLogin = APIRouter()

class Admin(BaseModel):
    email: str = Field(default='Mail de administrador', min_length=12, max_length=35)
    password: str = Field(default='Contraseña', min_length=3, max_length=30)



@routersLogin.post('/Login', tags=['Autenticacion'])
def autenticar_login(admin: Admin):
    try:
        if admin.email == 'aestheticestetica22@gmail.com' and admin.password == 'esteticaaesthetic2024': 
            token: str = createToken(admin.dict())
            print(token)
            return JSONResponse(content={"token": token})
        else:  
            return JSONResponse(content={"error": "Invalid credentials"}, status_code=401)

    except Exception as e:
        return JSONResponse(content={"error": str(e)}, status_code=500)
