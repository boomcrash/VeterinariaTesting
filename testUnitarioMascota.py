import pytest
from fastapi import HTTPException
from clases.mascotaClass import mascotaClass
from controladores.mascotaController import (
    getMascotas,
    getMascotasByTipoAnimal,
    insertarMascota,
    actualizarMascota
)


@pytest.mark.asyncio
async def test_get_mascotas():
    response = await getMascotas()
    assert response['accion'] is True
    assert 'data' in response and len(response['data']) > 0
    for mascota in response['data']:
        assert 'idMascota' in mascota
        assert 'nombre' in mascota
        assert 'edad' in mascota
        assert 'raza' in mascota
        assert 'colorPelaje' in mascota
        assert 'colorOjos' in mascota
        assert 'tipoAnimal' in mascota

@pytest.mark.asyncio
async def test_get_mascotas_by_tipoAnimal():
    response = await getMascotasByTipoAnimal("Gato")
    assert response['accion'] is True
    assert 'data' in response and len(response['data']) > 0
    for mascota in response['data']:
        assert 'idMascota' in mascota
        assert 'nombre' in mascota
        assert 'edad' in mascota
        assert 'raza' in mascota
        assert 'colorPelaje' in mascota
        assert 'colorOjos' in mascota
        assert 'tipoAnimal' in mascota


@pytest.mark.asyncio
async def test_insertar_mascota():
    mascota_data = mascotaClass(
        nombre='Mascota Prueba',
        edad=2,
        raza='Mascota Prueba',
        colorPelaje='Mascota Prueba',
        colorOjos='Mascota Prueba',
        tipoAnimal='Mascota Prueba'
    )
    response = await insertarMascota(mascota_data)
    assert response['accion'] is True


@pytest.mark.asyncio
async def test_actualizar_mascota():
    id_mascota = 1
    mascota_data = mascotaClass(
        nombre='Max',
        edad=3,
        raza='Labrador Retriever',
        colorPelaje='Dorado',
        colorOjos='Marrón',
        tipoAnimal='Perro'
    )
    response = await actualizarMascota(id_mascota, mascota_data)
    assert response['accion'] is True