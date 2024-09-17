# app/schemas.py
from pydantic import BaseModel, Field, validator
from typing import Optional
from datetime import date, datetime

class ProductBase(BaseModel):
    nombre: str = Field(..., min_length=3, max_length=100)
    descripcion: Optional[str] = Field(None, max_length=500)
    precio: float = Field(..., gt=0)
    categoria: str
    inventario: int = Field(..., ge=0)
    sku: str = Field(..., min_length=6, max_length=20)
    fecha_lanzamiento: Optional[date] = None
    imagen_url: Optional[str] = None

    @validator('sku')
    def validate_sku(cls, v):
        if not v.replace('-', '').isalnum():
            raise ValueError('SKU debe contener solo letras, números y guiones')
        return v

    @validator('precio')
    def validate_precio(cls, v):
        return round(v, 2)

    @validator('fecha_lanzamiento', pre=True)
    def validate_fecha_lanzamiento(cls, v):
        if v is None:
            return None
        if isinstance(v, date):
            return v
        if isinstance(v, str):
            try:
                return datetime.strptime(v, "%m/%d/%Y").date()
            except ValueError:
                raise ValueError("La fecha debe estar en formato MM/DD/YYYY")
        raise ValueError("Formato de fecha no válido")

    class Config:
        json_encoders = {
            date: lambda v: v.strftime("%m/%d/%Y") if v else None
        }

# Definición de la clase para crear un nuevo producto, que hereda de ProductBase
class ProductCreate(ProductBase):
    pass

# Definición de la clase para actualizar un producto existente, que hereda de ProductBase
class ProductUpdate(ProductBase):
    nombre: Optional[str] = Field(None, min_length=3, max_length=100)
    descripcion: Optional[str] = Field(None, max_length=500)
    precio: Optional[float] = Field(None, gt=0)
    categoria: Optional[str] = None
    inventario: Optional[int] = Field(None, ge=0)
    sku: Optional[str] = Field(None, min_length=6, max_length=20)

# Definición de la clase para la respuesta del producto, que hereda de ProductBase
class ProductResponse(ProductBase):
    id: str

    # Configuración para habilitar el modo ORM de Pydantic
    class Config:
        orm_mode = True