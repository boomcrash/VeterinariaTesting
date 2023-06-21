from pydantic import BaseModel


class propietarioClass(BaseModel):
    nombre: str = None
    apellido: str= None
    celular: str= None
    profesion: str= None
    edad: int= None