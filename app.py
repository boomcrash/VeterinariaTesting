
#importando controladores
from controladores.clienteController import cliente_router
from controladores.veterinariaController import veterinaria_router
from controladores.propietarioController import propietario_router
#libreria que se importa de configuracion.py (contiene las configuraciones del server)
from configuracion import configuracion
#inicializar flask con fastApi
from fastapi import  FastAPI,Request
#router
from fastapi import APIRouter
#uvicorn execute fastApi
import uvicorn
#pydantic para validar datos
from pydantic import BaseModel
# parametros de peticiones http en body
from fastapi.param_functions import Body
# evitar cors
from fastapi.middleware.cors import CORSMiddleware

#inicializar fastApi
app=FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)



#entrega_router
app.include_router(
    cliente_router,
    prefix='/api/v1/cliente',
    tags=['cliente'],
    responses={404: {'description': 'Error de acceso a la ventana de entregas'}},
)

#veterinaria_router
app.include_router(
    veterinaria_router,
    prefix='/api/v1/veterinaria',
    tags=['veterinaria'],
    responses={404: {'description': 'Error de acceso a la ventana de veterinaria'}},
)

app.include_router(
    propietario_router,
    prefix='/api/v1/propietario',
    tags=['propietario'],
    responses={404: {'description': 'Error de acceso a la ventana de propietarios'}},
)

#app.include_router(user_router, prefix="/api/v1")

if __name__=="__main__":
    uvicorn.run(app,host=configuracion['development'].HOST,port=configuracion['development'].PORT)