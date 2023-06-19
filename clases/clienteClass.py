from pydantic import BaseModel


class clienteClass(BaseModel):
    nombre: str = None
    apellido: str = None
    cedula: str = None
    edad: int = None
    ciudad: str= None