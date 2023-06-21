from fastapi import  FastAPI,Request,HTTPException
from fastapi import APIRouter
#pydantic para validar datos
from pydantic import BaseModel
# parametros de peticiones http en body
from fastapi.param_functions import Body
#importacion de clases de usuario
from clases.propietarioClass import propietarioClass

#importando conexion
import conexion
propietario_router = APIRouter()

from fastapi import HTTPException

@propietario_router.get("/getPropietarios")
async def getPropietarios():
    conn = await conexion.getConexion()
    try:
        propietarios = []
        async with conn.cursor() as cur:
            await cur.execute("SELECT * FROM propietario")
            result = await cur.fetchall()
            for data in result:
                propietario = {'idPropietario': data['idPropietario'], 'nombre': data['nombre'], 'apellido': data['apellido'], 'celular': data['celular'], 'profesion': data['profesion'], 'edad': data['edad']}
                propietarios.append(propietario)
        if len(propietarios) > 0:
            return {'data': propietarios, 'accion': True}
        else:
            raise HTTPException(status_code=404, detail="Not Found")
    except Exception as e:
        raise HTTPException(status_code=500, detail="")
    finally:
        conn.close()

@propietario_router.get("/getpropietariosByNombre")
async def getpropietariosByNombre(nombre: str):
    conn = await conexion.getConexion()
    try:
        propietarios = []
        async with conn.cursor() as cur:
            await cur.execute("SELECT * FROM propietario WHERE nombre LIKE %s", ('%' + nombre + '%',))
            result = await cur.fetchall()
            for data in result:
                propietario = {'idPropietario': data['idPropietario'], 'nombre': data['nombre'], 'apellido': data['apellido'], 'celular': data['celular'], 'profesion': data['profesion'], 'edad': data['edad']}
                propietarios.append(propietario)
        if len(propietarios) > 0:
            return {'data': propietarios, 'accion': True}
        else:
            raise HTTPException(status_code=404, detail="Not Found")
    except HTTPException:
        raise  # Re-raise the HTTPException
    except Exception as e:
        raise HTTPException(status_code=500, detail="")
    finally:
        conn.close()


@propietario_router.get("/getpropietariosByCelular")
async def getpropietariosByCelular(celular: str):
    conn = await conexion.getConexion()
    try:
        propietarios = []
        async with conn.cursor() as cur:
            await cur.execute("SELECT * FROM propietario WHERE celular =" + celular )
            result = await cur.fetchall()
            for data in result:
                propietario = {'idPropietario': data['idPropietario'], 'nombre': data['nombre'], 'apellido': data['apellido'], 'celular': data['celular'], 'profesion': data['profesion'], 'edad': data['edad']}
                propietarios.append(propietario)
        if len(propietarios) > 0:
            return {'data': propietarios, 'accion': True}
        else:
            raise HTTPException(status_code=404, detail="Not Found")
    except HTTPException:
        raise  # Re-raise the HTTPException
    except Exception as e:
        raise HTTPException(status_code=500, detail="")
    finally:
        conn.close()


@propietario_router.post("/insertarpropietario")
async def insertarpropietario(propietario:propietarioClass):
    conn = await conexion.getConexion()
    try:
        async with conn.cursor() as cur:
            await cur.execute("INSERT INTO propietario (nombre, apellido, celular, profesion, edad ) VALUES (%s, %s, %s, %s, %s)",
                              (propietario.nombre, propietario.apellido, propietario.celular, propietario.profesion, propietario.edad))
            await conn.commit()
        return {'mensaje': 'propietario insertado correctamente', 'accion': True}
    except Exception as e:
        raise HTTPException(status_code=500, detail="")
    finally:
        conn.close()


@propietario_router.put("/actualizarpropietario/{idPropietario}")
async def actualizarpropietario(idPropietario: int, propietario: propietarioClass):
    conn = await conexion.getConexion()
    try:
        async with conn.cursor() as cur:
            # Realizar la actualización del propietario
            await cur.execute("UPDATE propietario SET nombre = %s, apellido = %s, celular = %s, profesion = %s, edad = %s WHERE idPropietario = %s",
                              (propietario.nombre, propietario.apellido, propietario.celular, propietario.profesion, propietario.edad, idPropietario))
            
            if cur.rowcount > 0:
                await conn.commit()
                return {'mensaje': 'propietario actualizado correctamente', 'accion': True}
            else:
                raise HTTPException(status_code=404, detail="Not Found")
            
    except HTTPException:
        raise  # Re-raise the HTTPException
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        conn.close()


