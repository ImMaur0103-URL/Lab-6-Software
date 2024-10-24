from datetime import date, datetime
if __name__ == "utils":
    import json
    from typing import List
    from models import Product
    import os
    from datetime import date, datetime
else:
    import json
    from typing import List
    from APP.app.models import Product
    import os
    from datetime import date, datetime


# Definición de la función para cargar los productos desde el archivo JSON
def load_products(PRODUCTS_FILE) -> List[Product]:
    try:
        with open(PRODUCTS_FILE, "r") as f:
            products_data = json.load(f)
        return [Product.model_validate(p) for p in products_data]
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        print("Error al decodificar el JSON. Verifica el formato del archivo.")
        return []
    
def format_date(date_input):
    """Convert date from datetime object or string (YYYY-MM-DD) to MM/DD/YYYY format."""
    if isinstance(date_input, date):  # If it's a datetime.date or datetime object
        return date_input.strftime("%m/%d/%Y")
    elif isinstance(date_input, str):  # If it's a string (assumed to be in YYYY-MM-DD format)
        try:
            # Convert string to datetime object
            date_obj = datetime.strptime(date_input, "%Y-%m-%d")
            # Format and return the date in MM/DD/YYYY
            return date_obj.strftime("%m/%d/%Y")
        except ValueError:
            return date_input  # Return the original string if parsing fails
    else:
        return date_input  # If it's not a date or string, return as is

# Definición de la función para guardar los productos en el archivo JSON
def save_products(PRODUCTS_FILE, products: List[Product]):
    # Conversión de los objetos de Producto a diccionarios
    products_data = []
    for p in products:
        products_data.append({
            "id":p.id,
            "nombre":p.nombre,
            "descripcion":p.descripcion,
            "precio":p.precio,
            "categoria":p.categoria,
            "inventario":p.inventario,
            "sku":p.sku,
            "fecha_lanzamiento": p.fecha_lanzamiento.strftime("%m/%d/%Y"),
            "imagen_url":p.imagen_url
        })
    # Apertura del archivo JSON y guardado de los datos
    with open(PRODUCTS_FILE, "w") as f:
        json.dump(products_data, f, indent=2)

# No se devuelven líneas de código adicionales fuera del ámbito inmediato del bloque de código.