import py
from fastapi.testclient import TestClient
from app import app

client = TestClient(app)

# PRUEBAS TODO CORRECTO EN MODULO VETERINARIOS

def test_get_veterinaria():
    response = client.get("/api/v1/veterinaria/getVeterinaria")
    assert response.status_code == 200
    data = response.json()
    assert 'data' in data
    assert 'accion' in data
    assert data['accion'] is True
    assert 'data' in data and len(data['data']) > 0
    for veterinaria in data['data']:
        assert 'idVeterinaria' in veterinaria
        assert 'nombre' in veterinaria
        assert 'direccion' in veterinaria
        assert 'ruc' in veterinaria
        assert 'telefono' in veterinaria
        assert 'descripcion' in veterinaria

def test_get_veterinaria_by_id():
    response = client.get("/api/v1/veterinaria/getVeterinaria?idVeterinaria=1")
    assert response.status_code == 200
    data = response.json()
    assert 'data' in data
    assert 'accion' in data
    assert data['accion'] is True
    assert 'data' in data and len(data['data']) > 0
    for veterinaria in data['data']:
        assert 'idVeterinaria' in veterinaria
        assert 'nombre' in veterinaria
        assert 'direccion' in veterinaria
        assert 'ruc' in veterinaria
        assert 'telefono' in veterinaria
        assert 'descripcion' in veterinaria
    

def test_insertar_veterinaria():
    veterinaria_data = {
        'nombre': 'Clinica CatDog',
        'direccion': 'Cdla. La Garzota',
        'ruc': 1347854325678,
        'telefono': '0987654321',
        'descripcion': 'Clinica para mascotas'
    }
    response = client.post("/api/v1/veterinaria/insertarVeterinaria", json=veterinaria_data)
    assert response.status_code == 200
    data = response.json()
    assert 'mensaje' in data
    assert 'accion' in data
    assert data['accion'] is True
    #assert data['mensaje'] == 'Veterinaria insertada correctamente'


def test_actualizar_veterinaria():
    id_veterinaria = 28
    veterinaria_data = {
        'nombre': 'Veterinaria CatDog',
        'direccion': 'Cdla. La Garzota',
        'ruc': 1347854325678,
        'telefono': '0987654321',
        'descripcion': 'Clinica para mascotas'
    }
    response = client.put(f"/api/v1/veterinaria/actualizarVeterinaria/{id_veterinaria}", json=veterinaria_data)
    assert response.status_code == 200
    data = response.json()
    assert 'mensaje' in data
    assert 'accion' in data
    assert data['accion'] is True
    #assert data['mensaje'] == 'Veterinaria actualizada correctamente'

