from pydantic import BaseModel


class veterinariaClass(BaseModel):
    nombre: str = None
    direccion: str = None
    ruc: int = None
    telefono: str= None
    descripcion: str= None