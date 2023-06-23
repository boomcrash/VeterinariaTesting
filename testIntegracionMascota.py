import pytest
from fastapi.testclient import TestClient
from app import app

pet = TestClient(app)

#PRUEBAS TODO CORRECTO EN MODULO MASCOTAS

def test_get_mascotas():
    response = pet.get("/api/v1/mascota/getMascota")
    assert response.status_code == 200
    data = response.json()
    assert 'data' in data
    assert 'accion' in data
    assert data['accion'] is True
    assert 'data' in data and len(data['data']) > 0
    for mascota in data['data']:
        assert 'idMascota' in mascota
        assert 'nombre' in mascota
        assert 'edad' in mascota
        assert 'raza' in mascota
        assert 'colorPelaje' in mascota
        assert 'colorOjos' in mascota
        assert 'tipoAnimal' in mascota


def test_get_mascotas_by_tipoAnimal():
    response = pet.get("/api/v1/mascota/getMascotasByTipoAnimal?tipoAnimal=gato")
    assert response.status_code == 200
    data = response.json()
    assert 'data' in data
    assert 'accion' in data
    assert data['accion'] is True
    assert 'data' in data and len(data['data']) > 0
    for mascota in data['data']:
        assert 'idMascota' in mascota
        assert 'nombre' in mascota
        assert 'edad' in mascota
        assert 'raza' in mascota
        assert 'colorPelaje' in mascota
        assert 'colorOjos' in mascota
        assert 'tipoAnimal' in mascota


def test_insertar_mascota():
    mascota_data = {
        'nombre': 'Mascota Prueba',
        'edad': 6,
        'raza': 'Mascota Prueba',
        'colorPelaje': 'Mascota Prueba',
        'colorOjos': 'Mascota Prueba',
        'tipoAnimal': 'Mascota Prueba'
    }
    response = pet.post("/api/v1/mascota/insertarMascota", json=mascota_data)
    assert response.status_code == 200
    data = response.json()
    assert 'mensaje' in data
    assert 'accion' in data
    assert data['accion'] is True
    assert data['mensaje'] == 'Mascota insertado correctamente'


def test_actualizar_mascota():
    id_mascota = 12
    mascota_data = {
    'nombre': 'lolo',
    'edad': 6,
    'raza': 'Salchicha',
    'colorPelaje': 'Marrón',
    'colorOjos': 'Marrón',
    'tipoAnimal': 'Perro'
    }
    response = pet.put(f"/api/v1/mascota/actualizarMascota/{id_mascota}", json=mascota_data)
    assert response.status_code == 200
    data = response.json()
    assert 'mensaje' in data
    assert 'accion' in data
    assert data['accion'] is True
    assert data['mensaje'] == 'Mascota actualizado correctamente'