import pytest
from fastapi import HTTPException
from clases.veterinariaClass import veterinariaClass
from clases.veterinariaClass import veterinariaClass
from controladores.veterinariaController import (
    getVeterinaria,
    getVeterinariaById,
    insertarveterinaria,
    actualizarVeterinaria
)

# Pruebas unitarias para validar error 404

@pytest.mark.asyncio
async def test_get_veterinaria():
    response = await getVeterinaria()
    assert response['accion'] is True
    assert 'data' in response and len(response['data']) > 0
    for veterinaria in response['data']:
        assert 'idVeterinaria' in veterinaria
        assert 'nombre' in veterinaria
        assert 'direccion' in veterinaria
        assert 'ruc' in veterinaria
        assert 'telefono' in veterinaria
        assert 'descripcion' in veterinaria


@pytest.mark.asyncio
async def test_get_veterinaria_by_id():
    response = await getVeterinariaById(1)
    assert response['accion'] is True


@pytest.mark.asyncio
async def test_insertar_veterinaria():
    veterinaria = veterinariaClass(
        nombre="Clinica Cat",
        direccion="Duran",
        ruc=1234567890,
        telefono="0945388234",
        descripcion="Clinica para mininos",
    )
    response = await insertarveterinaria(veterinaria)
    assert response['accion'] is True


@pytest.mark.asyncio
async def test_actualizar_veterinaria():
    idVeterinaria = 1
    veterinaria = veterinariaClass(
        nombre="Clinica Pet",
        direccion="Duran",
        ruc=1234567890,
        telefono="0945388234",
        descripcion="Clinica para mascotas",
    )
    response = await actualizarVeterinaria(idVeterinaria, veterinaria)
    assert response['accion'] is True