from fastapi import  FastAPI,Request,HTTPException
from fastapi import APIRouter
#pydantic para validar datos
from pydantic import BaseModel
# parametros de peticiones http en body
from fastapi.param_functions import Body
#importacion de clases de usuario
from clases.clienteClass import clienteClass

#importando conexion
import conexion
cliente_router = APIRouter()

from fastapi import HTTPException

@cliente_router.get("/getClientes")
async def getClientes():
    conn = await conexion.getConexion()
    try:
        clientes = []
        async with conn.cursor() as cur:
            await cur.execute("SELECT * FROM cliente")
            result = await cur.fetchall()
            for data in result:
                cliente = {'idCliente': data['idCliente'], 'nombre': data['nombre'], 'apellido': data['apellido'], 'cedula': data['cedula'], 'edad': data['edad'], 'ciudad': data['ciudad']}
                clientes.append(cliente)
        if len(clientes) > 0:
            return {'data': clientes, 'accion': True}
        else:
            raise HTTPException(status_code=404, detail="Not Found")
    except Exception as e:
        raise HTTPException(status_code=500, detail="")
    finally:
        conn.close()


@cliente_router.get("/getClientes/{idCliente}")
async def getClientesById(idCliente: int):
    conn = await conexion.getConexion()
    try:
        async with conn.cursor() as cur:
            await cur.execute("SELECT * FROM cliente WHERE idCliente = %s", (idCliente,))
            result = await cur.fetchone()
            if result is not None:
                cliente = {'idCliente': result['idCliente'], 'nombre': result['nombre'], 'apellido': result['apellido'], 'cedula': result['cedula'], 'edad': result['edad'], 'ciudad': result['ciudad']}
                return {'data': cliente, 'accion': True}
            else:
                raise HTTPException(status_code=404, detail="Not Found")
    except HTTPException:
        raise  # Re-raise the HTTPException
    except Exception as e:
        raise HTTPException(status_code=500, detail="")
    finally:
        conn.close()


@cliente_router.get("/getClientesByNombre")
async def getClientesByNombre(nombre: str):
    conn = await conexion.getConexion()
    try:
        clientes = []
        async with conn.cursor() as cur:
            await cur.execute("SELECT * FROM cliente WHERE nombre LIKE %s", ('%' + nombre + '%',))
            result = await cur.fetchall()
            for data in result:
                cliente = {'idCliente': data['idCliente'], 'nombre': data['nombre'], 'apellido': data['apellido'], 'cedula': data['cedula'], 'edad': data['edad'], 'ciudad': data['ciudad']}
                clientes.append(cliente)
        if len(clientes) > 0:
            return {'data': clientes, 'accion': True}
        else:
            raise HTTPException(status_code=404, detail="Not Found")
    except HTTPException:
        raise  # Re-raise the HTTPException
    except Exception as e:
        raise HTTPException(status_code=500, detail="")
    finally:
        conn.close()


@cliente_router.get("/getClientesByCiudad")
async def getClientesByCiudad(ciudad: str):
    conn = await conexion.getConexion()
    try:
        clientes = []
        async with conn.cursor() as cur:
            await cur.execute("SELECT * FROM cliente WHERE ciudad LIKE %s", ('%' + ciudad + '%',))
            result = await cur.fetchall()
            for data in result:
                cliente = {'idCliente': data['idCliente'], 'nombre': data['nombre'], 'apellido': data['apellido'], 'cedula': data['cedula'], 'edad': data['edad'], 'ciudad': data['ciudad']}
                clientes.append(cliente)
        if len(clientes) > 0:
            return {'data': clientes, 'accion': True}
        else:
            raise HTTPException(status_code=404, detail="Not Found")
    except HTTPException:
        raise  # Re-raise the HTTPException
    except Exception as e:
        raise HTTPException(status_code=500, detail="")
    finally:
        conn.close()


@cliente_router.post("/insertarCliente")
async def insertarCliente(cliente:clienteClass):
    conn = await conexion.getConexion()
    try:
        async with conn.cursor() as cur:
            await cur.execute("INSERT INTO cliente (nombre, apellido, cedula, edad, ciudad) VALUES (%s, %s, %s, %s, %s)",
                              (cliente.nombre, cliente.apellido, cliente.cedula, cliente.edad, cliente.ciudad))
            await conn.commit()
        return {'mensaje': 'Cliente insertado correctamente', 'accion': True}
    except Exception as e:
        raise HTTPException(status_code=500, detail="")
    finally:
        conn.close()


@cliente_router.put("/actualizarCliente/{idCliente}")
async def actualizarCliente(idCliente: int, cliente: clienteClass):
    conn = await conexion.getConexion()
    try:
        async with conn.cursor() as cur:
            # Realizar la actualización del cliente
            await cur.execute("UPDATE cliente SET nombre = %s, apellido = %s, cedula = %s, edad = %s, ciudad = %s WHERE idCliente = %s",
                              (cliente.nombre, cliente.apellido, cliente.cedula, cliente.edad, cliente.ciudad, idCliente))
            
            if cur.rowcount > 0:
                await conn.commit()
                return {'mensaje': 'Cliente actualizado correctamente', 'accion': True}
            else:
                raise HTTPException(status_code=404, detail="Not Found")
            
    except HTTPException:
        raise  # Re-raise the HTTPException
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        conn.close()


