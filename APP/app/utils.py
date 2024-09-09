import json
from typing import List
from .models import Product

# Definición de la ruta del archivo JSON para almacenar los productos
PRODUCTS_FILE = "data/productos.json"

# Definición de la función para cargar los productos desde el archivo JSON
def load_products() -> List[Product]:
    try:
        # Apertura del archivo JSON y carga de los datos
        with open(PRODUCTS_FILE, "r") as f:
            products_data = json.load(f)
        # Conversión de los datos a objetos de Producto y retorno de la lista de productos
        return [Product(**p) for p in products_data]
    except FileNotFoundError:
        # Devolución de una lista vacía si el archivo JSON no existe
        return []

# Definición de la función para guardar los productos en el archivo JSON
def save_products(products: List[Product]):
    # Conversión de los objetos de Producto a diccionarios
    products_data = [p.dict() for p in products]
    # Apertura del archivo JSON y guardado de los datos
    with open(PRODUCTS_FILE, "w") as f:
        json.dump(products_data, f, indent=2, default=str)

# No se devuelven líneas de código adicionales fuera del ámbito inmediato del bloque de código.