from fastapi import  FastAPI,Request,HTTPException
from fastapi import APIRouter
#pydantic para validar datos
from pydantic import BaseModel
# parametros de peticiones http en body
from fastapi.param_functions import Body
#importacion de clases de usuario
from clases.veterinariaClass import veterinariaClass

#importando conexion
import conexion
veterinaria_router = APIRouter()

from fastapi import HTTPException

@veterinaria_router.get("/getVeterinaria")
async def getVeterinaria():
    conn = await conexion.getConexion()
    try:
        veterinarias = []
        async with conn.cursor() as cur:
            await cur.execute("SELECT * FROM veterinaria")
            result = await cur.fetchall()
            for data in result:
                veterinaria = {'idVeterinaria': data['idVeterinaria'], 'nombre': data['nombre'], 'direccion': data['direccion'], 'ruc': data['ruc'], 'telefono': data['telefono'], 'descripcion': data['descripcion']}
                veterinarias.append(veterinaria)
        if len(veterinarias) > 0:
            return {'data': veterinarias, 'accion': True}
        else:
            raise HTTPException(status_code=404, detail="Not Found")
    except Exception as e:
        raise HTTPException(status_code=500, detail="")
    finally:
        conn.close()


@veterinaria_router.post("/insertarVeterinaria")
async def insertarCliente(veterinaria:veterinariaClass):
    conn = await conexion.getConexion()
    try:
        async with conn.cursor() as cur:
            await cur.execute("INSERT INTO veterinaria (nombre, direccion, ruc, telefono, descripcion) VALUES (%s, %s, %s, %s, %s)",
                              (veterinaria.nombre, veterinaria.direccion, veterinaria.ruc, veterinaria.telefono, veterinaria.descripcion))
            await conn.commit()
        return {'mensaje': 'Veterinaria insertado correctamente', 'accion': True}
    except Exception as e:
        raise HTTPException(status_code=500, detail="")
    finally:
        conn.close()