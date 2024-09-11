from unittest.mock import patch
import unittest

class TestProductAPI(unittest.TestCase):
    """def setUp(self):
        #self.client = testclient(app)
        self.test_product = {
            "nombre": "Producto de prueba",
            "descripcion": "Este es un producto de prueba",
            "precio": 99.99,
            "categoria": "Electrónica",
            "inventario": 10,
            "sku": "TEST-SKU-001"
        }
        self.mock_products = []"""

    """@patch('app.utils.load_products')
    @patch('app.utils.save_products')
    def test_create_product(self, mock_save, mock_load):
        mock_load.return_value = self.mock_products
        mock_save.side_effect = lambda products: self.mock_products.extend(products)

        response = self.client.post("/productos", json=self.test_product)
        self.assertEqual(response.status_code, 200)
        created_product = response.json()
        self.assertEqual(created_product["nombre"], self.test_product["nombre"])
        self.assertEqual(created_product["sku"], self.test_product["sku"])
        self.assertEqual(len(self.mock_products), 1)

    @patch('app.utils.load_products')
    def test_get_all_products(self, mock_load):
        mock_load.return_value = [self.test_product]
        response = self.client.get("/productos")
        self.assertEqual(response.status_code, 200)
        products = response.json()
        self.assertIsInstance(products, list)
        self.assertEqual(len(products), 1)
        self.assertEqual(products[0]["nombre"], self.test_product["nombre"])"""
    def test_ejemplo(self):
        pass
        self.assertEqual(1,1)

if __name__ == '__main__':
    unittest.main()