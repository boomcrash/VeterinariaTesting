import pytest
from fastapi import HTTPException
from clases.clienteClass import clienteClass
from controladores.clienteController import (
    getClientes,
    getClientesByNombre,
    getClientesById,
    getClientesByCiudad,
    insertarCliente,
    actualizarCliente
)
from clases.propietarioClass import propietarioClass
from controladores.propietarioController import (
    getPropietarios,
    getpropietariosByNombre,
    getpropietariosByCelular,
    getpropietariosByProfesion,
    insertarPropietario,
    actualizarPropietario
)

# Pruebas unitarias para validar error 404

@pytest.mark.asyncio
async def test_get_clients_by_name_error_404():
    with pytest.raises(HTTPException) as exc_info:
        await getClientesByNombre("asdacas")
    assert exc_info.value.status_code == 404
    assert str(exc_info.value.detail) == "Not Found"

@pytest.mark.asyncio
async def test_get_propietarios_by_id_error_404():
    with pytest.raises(HTTPException) as exc_info:
        await getpropietariosByNombre("Emely")
    assert exc_info.value.status_code == 404
    assert str(exc_info.value.detail) == "Not Found"

# Resto de pruebas unitarias

@pytest.mark.asyncio
async def test_get_clients():
    response = await getClientes()
    assert response['accion'] is True
    assert 'data' in response and len(response['data']) > 0
    for cliente in response['data']:
        assert 'idCliente' in cliente
        assert 'nombre' in cliente
        assert 'apellido' in cliente
        assert 'cedula' in cliente
        assert 'edad' in cliente
        assert 'ciudad' in cliente

@pytest.mark.asyncio
async def test_get_propietarios():
    response = await getPropietarios()
    assert response['accion'] is True
    assert 'data' in response and len(response['data']) > 0
    for propietario in response['data']:
        assert 'idPropietario' in propietario
        assert 'nombre' in propietario
        assert 'celular' in propietario
        assert 'profesion' in propietario
        assert 'edad' in propietario



@pytest.mark.asyncio
async def test_get_clients_by_name():
    response = await getClientesByNombre("carlos")
    assert response['accion'] is True
    assert 'data' in response and len(response['data']) > 0
    for cliente in response['data']:
        assert 'idCliente' in cliente
        assert 'nombre' in cliente
        assert 'apellido' in cliente
        assert 'cedula' in cliente
        assert 'edad' in cliente
        assert 'ciudad' in cliente

@pytest.mark.asyncio
async def test_get_propietarios_by_name():
    response = await getpropietariosByNombre("Henry")
    assert response['accion'] is True
    assert 'data' in response and len(response['data']) > 0
    for propietario in response['data']:
        assert 'idPropietario' in propietario
        assert 'nombre' in propietario
        assert 'celular' in propietario
        assert 'profesion' in propietario
        assert 'edad' in propietario

@pytest.mark.asyncio
async def test_get_clients_by_id():
    response = await getClientesById(1)
    assert response['accion'] is True

@pytest.mark.asyncio
async def test_get_propietarios_by_id():
    response = await getpropietariosByCelular("0992249693")
    assert response['accion'] is True

@pytest.mark.asyncio
async def test_get_clients_by_city():
    response = await getClientesByCiudad("guayaquil")
    assert response['accion'] is True
    assert 'data' in response and len(response['data']) > 0
    for cliente in response['data']:
        assert 'idCliente' in cliente
        assert 'nombre' in cliente
        assert 'apellido' in cliente
        assert 'cedula' in cliente
        assert 'edad' in cliente
        assert 'ciudad' in cliente

@pytest.mark.asyncio
async def test_get_propietarios_by_profesion():
    response = await getpropietariosByProfesion("Programador")
    assert response['accion'] is True
    assert 'data' in response and len(response['data']) > 0
    for propietario in response['data']:
        assert 'idPropietario' in propietario
        assert 'nombre' in propietario
        assert 'celular' in propietario
        assert 'profesion' in propietario
        assert 'edad' in propietario

@pytest.mark.asyncio
async def test_insertar_cliente():
    cliente_data = clienteClass(
        nombre='Johny',
        apellido='Doew',
        cedula='123333789',
        edad=30,
        ciudad='Ciudad Prueba'
    )
    response = await insertarCliente(cliente_data)
    assert response['accion'] is True

@pytest.mark.asyncio
async def test_insertar_propietario():
    propietario_data = propietarioClass(
        nombre='Johansson',
        apellido='Doew',
        celular='123333789',
        profesion='Investigador',
        edad=30,
    )
    response = await insertarPropietario(propietario_data)
    assert response['accion'] is True

@pytest.mark.asyncio
async def test_actualizar_cliente():
    id_cliente = 1
    cliente_data = clienteClass(
        nombre='Johny3',
        apellido='Doew2',
        cedula='123333789',
        edad=30,
        ciudad='Ciudad Prueba'
    )
    response = await actualizarCliente(id_cliente, cliente_data)
    assert response['accion'] is True

@pytest.mark.asyncio
async def test_actualizar_propietario():
    id_propietario = 12
    propietario_data = propietarioClass(
        nombre='John',
        apellido='Doew',
        celular='123333789',
        profesion='Investigador',
        edad=30,
    )
    response = await actualizarPropietario(id_propietario, propietario_data)
    assert response['accion'] is True
