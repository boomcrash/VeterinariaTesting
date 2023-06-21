from pydantic import BaseModel


class mascotaClass(BaseModel):
    nombre: str = None
    edad: int = None
    raza: str = None
    colorPelaje: str = None
    colorOjos: str= None
    tipoAnimal: str= None