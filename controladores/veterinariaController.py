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


@veterinaria_router.get("/getVeterinaria/{idVeterinaria}")
async def getVeterinariaById(idVeterinaria: int):
    conn = await conexion.getConexion()
    try:
        async with conn.cursor() as cur:
            await cur.execute("SELECT * FROM veterinaria WHERE idVeterinaria = %s", (idVeterinaria,))
            result = await cur.fetchone()
            if result is not None:
                veterinaria = {'idVeterinaria': result['idVeterinaria'], 'nombre': result['nombre'], 'direccion': result['direcciono'], 'ruc': result['ruc'], 'telefono': result['telefono'], 'descripcion': result['descripcion']}
                return {'data': veterinaria, 'accion': True}
            else:
                raise HTTPException(status_code=404, detail="Not Found")
    except HTTPException:
        raise  # Re-raise the HTTPException
    except Exception as e:
        raise HTTPException(status_code=500, detail="")
    finally:
        conn.close()


@veterinaria_router.post("/insertarVeterinaria")
async def insertarveterinaria(veterinaria:veterinariaClass):
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

    
@veterinaria_router.put("/actualizarVeterinaria/{idVeterinaria}")
async def actualizarVeterinaria(idVeterinaria: int, veterinaria: veterinariaClass):
    conn = await conexion.getConexion()
    try:
        async with conn.cursor() as cur:
            await cur.execute("UPDATE veterinaria SET nombre = %s, direccion = %s, ruc = %s, telefono = %s, descripcion = %s WHERE idVeterinaria = %s",
                              (veterinaria.nombre, veterinaria.direccion, veterinaria.ruc, veterinaria.telefono, veterinaria.descripcion, idVeterinaria))
            if cur.rowcount > 0:
                await conn.commit()
                return {'mensaje': 'Veterinaria actualizado correctamente', 'accion': True}
            else:
                raise HTTPException(status_code=404, detail="Not Found")
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail="")
    finally:
        conn.close()