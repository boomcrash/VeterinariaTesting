from fastapi import  FastAPI,Request,HTTPException
from fastapi import APIRouter
#pydantic para validar datos
from pydantic import BaseModel
# parametros de peticiones http en body
from fastapi.param_functions import Body
#importacion de clases de usuario
from clases.mascotaClass import mascotaClass

#importando conexion
import conexion
mascota_router = APIRouter()

from fastapi import HTTPException

@mascota_router.get("/getMascota")
async def getMascotas():
    conn = await conexion.getConexion()
    try:
        mascotas = []
        async with conn.cursor() as cur:
            await cur.execute("SELECT * FROM mascota")
            result = await cur.fetchall()
            for data in result:
                mascota = {'idMascota': data['idMascota'], 'nombre': data['nombre'], 'edad': data['edad'], 'raza': data['raza'], 'colorPelaje': data['colorPelaje'], 'colorOjos': data['colorOjos'], 'tipoAnimal': data['tipoAnimal']}
                mascotas.append(mascota)
        if len(mascotas) > 0:
            return {'data': mascotas, 'accion': True}
        else:
            raise HTTPException(status_code=404, detail="Not Found")
    except Exception as e:
        raise HTTPException(status_code=500, detail="")
    finally:
        conn.close()


@mascota_router.get("/getMascotasByTipoAnimal")
async def getMascotasByTipoAnimal(tipoAnimal: str):
    conn = await conexion.getConexion()
    try:
        mascotas = []
        async with conn.cursor() as cur:
            await cur.execute("SELECT * FROM mascota WHERE tipoAnimal LIKE %s", ('%' + tipoAnimal + '%',))
            result = await cur.fetchall()
            for data in result:
                mascota = {'idMascota': data['idMascota'], 'nombre': data['nombre'], 'edad': data['edad'], 'raza': data['raza'], 'colorPelaje': data['colorPelaje'], 'colorOjos': data['colorOjos'], 'tipoAnimal': data['tipoAnimal']}
                mascotas.append(mascota)
        if len(mascotas) > 0:
            return {'data': mascotas, 'accion': True}
        else:
            raise HTTPException(status_code=404, detail="Not Found")
    except HTTPException:
        raise  # Re-raise the HTTPException
    except Exception as e:
        raise HTTPException(status_code=500, detail="")
    finally:
        conn.close()



@mascota_router.post("/insertarMascota")
async def insertarMascota(mascota:mascotaClass):
    conn = await conexion.getConexion()
    try:
        async with conn.cursor() as cur:
            await cur.execute("INSERT INTO mascota (nombre, edad, raza, colorPelaje, colorOjos, tipoAnimal ) VALUES (%s, %s, %s, %s, %s, %s)",
                              (mascota.nombre, mascota.edad, mascota.raza, mascota.colorPelaje, mascota.colorOjos, mascota.tipoAnimal))
            await conn.commit()
        return {'mensaje': 'Mascota insertado correctamente', 'accion': True}
    except Exception as e:
        raise HTTPException(status_code=500, detail="")
    finally:
        conn.close()


@mascota_router.put("/actualizarMascota/{idMascota}")
async def actualizarMascota(idMascota: int, mascota: mascotaClass):
    conn = await conexion.getConexion()
    try:
        async with conn.cursor() as cur:
            # Realizar la actualización de mascota
            await cur.execute("UPDATE mascota SET nombre = %s, edad = %s, raza = %s, colorPelaje = %s, colorOjos = %s, tipoAnimal = %s WHERE idMascota = %s",
                              (mascota.nombre, mascota.edad, mascota.raza, mascota.colorPelaje, mascota.colorOjos, mascota.tipoAnimal, idMascota))
            
            if cur.rowcount > 0:
                await conn.commit()
                return {'mensaje': 'Mascota actualizado correctamente', 'accion': True}
            else:
                raise HTTPException(status_code=404, detail="Not Found")
            
    except HTTPException:
        raise  # Re-raise the HTTPException
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        conn.close()