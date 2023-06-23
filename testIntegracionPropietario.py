import pytest
from fastapi.testclient import TestClient
from app import app

Propietario = TestClient(app)

#PRUEBAS TODO CORRECTO EN MODULO CLIENTES

def test_get_Propietarios():
    response = Propietario.get("/api/v1/propietario/getPropietarios")
    assert response.status_code == 200
    data = response.json()
    assert 'data' in data
    assert 'accion' in data
    assert data['accion'] is True
    assert 'data' in data and len(data['data']) > 0
    for propietario in data['data']:
        assert 'idPropietario' in propietario
        assert 'nombre' in propietario
        assert 'celular' in propietario
        assert 'profesion' in propietario
        assert 'edad' in propietario


def test_get_Propietarios_by_name():
    response = Propietario.get("/api/v1/propietario/getpropietariosByNombre?nombre=Milton")
    assert response.status_code == 200
    data = response.json()
    assert 'data' in data
    assert 'accion' in data
    assert data['accion'] is True
    assert 'data' in data and len(data['data']) > 0
    for propietario in data['data']:
        assert 'idPropietario' in propietario
        assert 'nombre' in propietario
        assert 'celular' in propietario
        assert 'profesion' in propietario
        assert 'edad' in propietario


def test_get_Propietarios_by_celular():
    response = Propietario.get("/api/v1/propietario/getpropietariosByCelular?celular=0992249693")
    assert response.status_code == 200
    data = response.json()
    assert 'data' in data
    assert 'accion' in data
    assert data['accion'] is True
    assert 'data' in data and len(data['data']) > 0
    for propietario in data['data']:
        assert 'idPropietario' in propietario
        assert 'nombre' in propietario
        assert 'celular' in propietario
        assert 'profesion' in propietario
        assert 'edad' in propietario


def test_get_Propietarios_by_profesion():
    response = Propietario.get("/api/v1/propietario/getpropietariosByProfesion?profesion=Programador")
    assert response.status_code == 200
    data = response.json()
    assert 'data' in data
    assert 'accion' in data
    assert data['accion'] is True
    assert 'data' in data and len(data['data']) > 0
    for propietario in data['data']:
        assert 'idPropietario' in propietario
        assert 'nombre' in propietario
        assert 'celular' in propietario
        assert 'profesion' in propietario
        assert 'edad' in propietario


def test_insertar_propietario():
    propietario_data = {
        'nombre': 'Johny',
        'apellido': 'Doew',
        'celular': '123333789',
        'profesion': 'Programador',
        'edad': 30
    }
    response = Propietario.post("/api/v1/propietario/insertarPropietario", json=propietario_data)
    assert response.status_code == 200
    data = response.json()
    assert 'mensaje' in data
    assert 'accion' in data
    assert data['accion'] is True
    assert data['mensaje'] == 'propietario insertado correctamente'


def test_actualizar_propietario():
    id_propietario = 12
    propietario_data = {
        'nombre': 'Johny',
        'apellido': 'Doew',
        'celular': '123333789',
        'profesion': 'Profesor',
        'edad': 30
    }
    response = Propietario.put(f"/api/v1/propietario/actualizarPropietario/{id_propietario}", json=propietario_data)
    assert response.status_code == 200
    data = response.json()
    assert 'mensaje' in data
    assert 'accion' in data
    assert data['accion'] is True
    assert data['mensaje'] == 'propietario actualizado correctamente'


# Pruebas unitarias para validar error 404

@pytest.fixture
def test_Propietario():
    with TestClient(app) as Propietario:
        yield Propietario

def test_get_Propietarios_by_name_error_404(test_Propietario):
    response = test_Propietario.get("/api/v1/propietario/getPropietariosByNombre?nombre=asdacas")
    assert response.status_code == 404
    assert response.json() == {"detail": "Not Found"}


def test_get_Propietarios_by_id_error_404(test_Propietario):
    response = test_Propietario.get("/api/v1/propietario/getPropietarios/3123123213")
    assert response.status_code == 404
    assert response.json() == {"detail": "Not Found"}


def test_get_Propietarios_by_city_error_404(test_Propietario):
    response = test_Propietario.get("/api/v1/propietario/getPropietariosByCiudad?ciudad=gasuhasa")
    assert response.status_code == 404
    assert response.json() == {"detail": "Not Found"}


def test_insertar_propietario_error_500(test_Propietario):
    propietario_data = {
        'nombre': 'Johny',
        'apellido': 'Doew',
        'celular': '123333789',
        'ciudad': 'Ciudad Prueba',
        'edad': 30
    }
    response = test_Propietario.post("/api/v1/propietario/insertarPropietario", json=propietario_data)
    assert response.status_code == 500
    assert response.json() == {"detail": ""}


def test_actualizar_propietario_error_404(test_Propietario):
    id_propietario = 121313213
    propietario_data = {
        'nombre': 'Johny',
        'apellido': 'Doew',
        'celular': '123333789',
        'ciudad': 'Ciudad Prueba',
        'edad': 30
    }
    response = test_Propietario.put(f"/api/v1/propietario/actualizarPropietario/{id_propietario}", json=propietario_data)
    assert response.status_code == 404
    assert response.json() == {"detail": "Not Found"}

# Ejecutar las pruebas
if __name__ == '__main__':
    pytest.main([__file__])
