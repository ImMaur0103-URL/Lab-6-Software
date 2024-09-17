from datetime import date, datetime
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
def save_products(products: List[Product]):
    # Convert product objects to dictionaries
    products_data = [p.model_dump() for p in products]
    
    # Update date fields to MM/DD/YYYY format
    for product in products_data:
        if 'fecha_lanzamiento' in product:  # Replace with your actual date field name
            product['fecha_lanzamiento'] = format_date(product['fecha_lanzamiento'])

    # Save products to a JSON file
    with open(PRODUCTS_FILE, "w") as f:
        json.dump(products_data, f, indent=2)

# No se devuelven líneas de código adicionales fuera del ámbito inmediato del bloque de código.