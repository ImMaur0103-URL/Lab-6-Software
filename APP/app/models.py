# Definición de modelos de datos para el producto
# app/models.py
from pydantic import BaseModel, Field, validator
from typing import Optional
from datetime import date
import uuid

class Product(BaseModel):
    id: str = Field(default_factory=lambda: str(uuid.uuid4()))
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

    @validator('fecha_lanzamiento')
    def validate_fecha_lanzamiento(cls, v):
        date.fromisoformat(v)
        if v and v < date.today():
            raise ValueError('La fecha de lanzamiento debe ser en el presente o futuro')
        return v