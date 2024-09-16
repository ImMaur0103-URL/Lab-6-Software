if __name__ == "utils":
    import json
    from typing import List
    from models import Product
    import os
else:
    import json
    from typing import List
    from app.models import Product
    import os

# Obtén la ruta absoluta del directorio del script actual
current_dir = os.path.dirname(os.path.abspath(__file__))

# Sube dos niveles en la jerarquía de directorios
project_root = os.path.dirname(current_dir)

PRODUCTS_FILE = str(project_root) + "\data\MOCK_DATA.json"

# Definición de la función para cargar los productos desde el archivo JSON
def load_products() -> List[Product]:
    try:
        with open(PRODUCTS_FILE, "r") as f:
            products_data = json.load(f)
        return [Product.model_validate(p) for p in products_data]
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        print("Error al decodificar el JSON. Verifica el formato del archivo.")
        return []

# Definición de la función para guardar los productos en el archivo JSON
def save_products(products: List[Product]):
    # Conversión de los objetos de Producto a diccionarios
    products_data = [p.dict() for p in products]
    # Apertura del archivo JSON y guardado de los datos
    with open(PRODUCTS_FILE, "w") as f:
        json.dump(products_data, f, indent=2, default=str)

# No se devuelven líneas de código adicionales fuera del ámbito inmediato del bloque de código.