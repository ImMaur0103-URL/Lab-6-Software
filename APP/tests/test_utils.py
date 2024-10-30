import unittest
from unittest.mock import patch, mock_open, MagicMock
import json
from datetime import date
from app.utils import load_products, save_products, format_date  # Importa desde el archivo utils
from app.models import Product  # Asegúrate de que Product esté correctamente importado
import os
from fastapi.testclient import TestClient

# Obtén la ruta absoluta del directorio del script actual
current_dir = os.path.dirname(os.path.abspath(__file__))

# Sube dos niveles en la jerarquía de directorios
project_root = os.path.dirname(current_dir)

PRODUCTS_FILE = str(project_root) + "\data\MOCK_DATA.json"

class TestUtils(unittest.TestCase):
    @patch('builtins.open', new_callable=mock_open, read_data='[]')
    def test_load_products_empty(self, mock_file):
        """Testea que la función load_products devuelva una lista vacía cuando el archivo está vacío."""
        products = load_products(PRODUCTS_FILE)
        self.assertEqual(products, [])
        mock_file.assert_called_once_with(PRODUCTS_FILE, "r")

    @patch('builtins.open', new_callable=mock_open, read_data='invalid json')
    def test_load_products_json_decode_error(self, mock_file):
        """Testea que load_products maneje el JSONDecodeError correctamente."""
        products = load_products(PRODUCTS_FILE)
        self.assertEqual(products, [])
        mock_file.assert_called_once_with(PRODUCTS_FILE, "r")

    @patch('builtins.open', new_callable=mock_open, read_data='[{"name": "Product 1"}]')
    @patch('APP.app.models.Product.model_validate', return_value=MagicMock())
    def test_load_products_success(self, mock_validate, mock_file):
        """Testea que load_products cargue los productos correctamente."""
        products = load_products(PRODUCTS_FILE)
        self.assertEqual(len(products), 1)
        mock_file.assert_called_once_with(PRODUCTS_FILE, "r")
        mock_validate.assert_called_once_with({"name": "Product 1"})

    def test_format_date_with_date_object(self):
        """Testea que format_date convierta correctamente un objeto date a MM/DD/YYYY."""
        date_obj = date(2024, 10, 24)
        formatted = format_date(date_obj)
        self.assertEqual(formatted, "10/24/2024")

    def test_format_date_with_string(self):
        """Testea que format_date convierta una fecha en formato YYYY-MM-DD a MM/DD/YYYY."""
        formatted = format_date("2024-10-24")
        self.assertEqual(formatted, "10/24/2024")

    def test_format_date_with_invalid_string(self):
        """Testea que format_date devuelva la cadena original si no puede parsearla."""
        formatted = format_date("invalid date")
        self.assertEqual(formatted, "invalid date")

    def test_format_date_with_other_type(self):
        """Testea que format_date devuelva el input original si no es string o date."""
        formatted = format_date(12345)
        self.assertEqual(formatted, 12345)

    @patch('builtins.open', new_callable=mock_open)
    @patch('APP.app.models.Product.model_dump', return_value={"name": "Product 1", "fecha_lanzamiento": "2024-10-24"})
    def test_save_products(self, mock_dump, mock_file):
        """Testea que save_products guarde correctamente los productos formateando la fecha."""
        product = Product(nombre="Product 1", precio=10, categoria='', inventario=0, sku='oiho3hf', fecha_lanzamiento=date(2024, 10, 24))
        save_products(PRODUCTS_FILE, [product])
        
        mock_file.assert_called_once_with(PRODUCTS_FILE, "w")

        # Verificar que la función write fue llamada y que el contenido es el correcto
        written_data = ''.join(call.args[0] for call in mock_file().write.mock_calls)
        
        # Comprobar que el contenido JSON contiene los datos esperados
        self.assertIn('"nombre": "Product 1"', written_data)
        self.assertIn('"fecha_lanzamiento": "10/24/2024"', written_data)

if __name__ == "__main__":
    unittest.main()
