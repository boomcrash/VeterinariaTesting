import pytest
from fastapi.testclient import TestClient
from app import app

client = TestClient(app)

#PRUEBAS TODO CORRECTO EN MODULO CLIENTES

def test_get_clients():
    response = client.get("/api/v1/cliente/getClientes")
    assert response.status_code == 200
    data = response.json()
    assert 'data' in data
    assert 'accion' in data
    assert data['accion'] is True
    assert 'data' in data and len(data['data']) > 0
    for cliente in data['data']:
        assert 'idCliente' in cliente
        assert 'nombre' in cliente
        assert 'apellido' in cliente
        assert 'cedula' in cliente
        assert 'edad' in cliente
        assert 'ciudad' in cliente


def test_get_clients_by_name():
    response = client.get("/api/v1/cliente/getClientesByNombre?nombre=carlos")
    assert response.status_code == 200
    data = response.json()
    assert 'data' in data
    assert 'accion' in data
    assert data['accion'] is True
    assert 'data' in data and len(data['data']) > 0
    for cliente in data['data']:
        assert 'idCliente' in cliente
        assert 'nombre' in cliente
        assert 'apellido' in cliente
        assert 'cedula' in cliente
        assert 'edad' in cliente
        assert 'ciudad' in cliente


def test_get_clients_by_id():
    response = client.get("/api/v1/cliente/getClientes?idCliente=1")
    assert response.status_code == 200
    data = response.json()
    assert 'data' in data
    assert 'accion' in data
    assert data['accion'] is True
    assert 'data' in data and len(data['data']) > 0
    for cliente in data['data']:
        assert 'idCliente' in cliente
        assert 'nombre' in cliente
        assert 'apellido' in cliente
        assert 'cedula' in cliente
        assert 'edad' in cliente
        assert 'ciudad' in cliente


def test_get_clients_by_city():
    response = client.get("/api/v1/cliente/getClientesByCiudad?ciudad=guayaquil")
    assert response.status_code == 200
    data = response.json()
    assert 'data' in data
    assert 'accion' in data
    assert data['accion'] is True
    assert 'data' in data and len(data['data']) > 0
    for cliente in data['data']:
        assert 'idCliente' in cliente
        assert 'nombre' in cliente
        assert 'apellido' in cliente
        assert 'cedula' in cliente
        assert 'edad' in cliente
        assert 'ciudad' in cliente


def test_insertar_cliente():
    cliente_data = {
        'nombre': 'Johny',
        'apellido': 'Doew',
        'cedula': '123333789',
        'edad': 30,
        'ciudad': 'Ciudad Prueba'
    }
    response = client.post("/api/v1/cliente/insertarCliente", json=cliente_data)
    assert response.status_code == 200
    data = response.json()
    assert 'mensaje' in data
    assert 'accion' in data
    assert data['accion'] is True
    assert data['mensaje'] == 'Cliente insertado correctamente'


def test_actualizar_cliente():
    id_cliente = 1
    cliente_data = {
    "nombre": "manolo5",
    "apellido": "rosa3",
    "cedula": "3333333333",
    "edad": 32,
    "ciudad": "Guayaquil"
    }
    response = client.put(f"/api/v1/cliente/actualizarCliente/{id_cliente}", json=cliente_data)
    assert response.status_code == 200
    data = response.json()
    assert 'mensaje' in data
    assert 'accion' in data
    assert data['accion'] is True
    assert data['mensaje'] == 'Cliente actualizado correctamente'


# Pruebas unitarias para validar error 404

@pytest.fixture
def test_client():
    with TestClient(app) as client:
        yield client

def test_get_clients_by_name_error_404(test_client):
    response = test_client.get("/api/v1/cliente/getClientesByNombre?nombre=asdacas")
    assert response.status_code == 404
    assert response.json() == {"detail": "Not Found"}


def test_get_clients_by_id_error_404(test_client):
    response = test_client.get("/api/v1/cliente/getClientes/3123123213")
    assert response.status_code == 404
    assert response.json() == {"detail": "Not Found"}


def test_get_clients_by_city_error_404(test_client):
    response = test_client.get("/api/v1/cliente/getClientesByCiudad?ciudad=gasuhasa")
    assert response.status_code == 404
    assert response.json() == {"detail": "Not Found"}


def test_insertar_cliente_error_500(test_client):
    cliente_data = {
        'apellido': 'Doew',
        'cedula': '123333789',
        'edad': 30,
        'ciudad': 'Ciudad Prueba'
    }
    response = test_client.post("/api/v1/cliente/insertarCliente", json=cliente_data)
    assert response.status_code == 500
    assert response.json() == {"detail": ""}


def test_actualizar_cliente_error_404(test_client):
    id_cliente = 121313213
    cliente_data = {
        'nombre': 'Jane4',
        'apellido': 'Doemand',
        'cedula': '987654321',
        'edad': 35,
        'ciudad': 'Quito'
    }
    response = test_client.put(f"/api/v1/cliente/actualizarCliente/{id_cliente}", json=cliente_data)
    assert response.status_code == 404
    assert response.json() == {"detail": "Not Found"}

# Ejecutar las pruebas
if __name__ == '__main__':
    pytest.main([__file__])
