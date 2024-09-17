from unittest.mock import patch
import os
import app.main as app
import app.models as models
import app.schemas as SCHEMA
import unittest
import json
import asyncio



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

#1. Creación de Producto (POST /productos): 
class TEST_1_Creación_Producto(unittest.TestCase):
    def setup(self):
        current_dir = os.path.dirname(os.path.abspath(__file__))
        project_root = os.path.dirname(current_dir)
        app.PRODUCTS_FILE = str(project_root) + "\data\MOCK_DATA_CREATE_TEST.json"

    def test_create_product(self):
        pass

#2. Lectura de Productos (GET /productos):
class TEST_2_Lectura_Productos(unittest.TestCase):
    def setUp(self):
        current_dir = os.path.dirname(os.path.abspath(__file__))
        project_root = os.path.dirname(current_dir)
        app.PRODUCTS_FILE = str(project_root) + "\data\MOCK_DATA.json"

    def test_read_products_no_filters(self):
        # Arrange
        expected_products_count = 1000

        # Act
        products = asyncio.run(app.read_products())

        # Assert
        self.assertEqual(len(products), expected_products_count)

    def test_read_products_name_filter(self):
        # Arrange
        expected_products_count = 3
        expected_products_json = [
            {
                "nombre": "Beans - Kidney, Red Dry",
                "descripcion": "Praesent blandit. Nam nulla. Integer pede justo, lacinia eget, tincidunt eget, tempus vel, pede.",
                "precio": 86.66,
                "categoria": "Notebook",
                "inventario": 97,
                "sku": "BVJXA-SKU-996",
                "fecha_lanzamiento": "11/30/2024",
                "imagen_url": "https://ejemplo.com/0p6xf.png",
                "id": "d1f486f0-6485-4a46-bc38-2657042bfabb"
            },
            {
                "nombre": "Beans - Kidney White",
                "descripcion": "Cum sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Vivamus vestibulum sagittis sapien. Cum sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus.\n\nEtiam vel augue. Vestibulum rutrum rutrum neque. Aenean auctor gravida sem.",
                "precio": 764.74,
                "categoria": "Water bottle",
                "inventario": 44,
                "sku": "PRLQX-SKU-160",
                "fecha_lanzamiento": "10/01/2025",
                "imagen_url": "https://ejemplo.com/kneb3.png",
                "id": "44e4396e-6b80-4278-97e1-94ee4143b78d"
            },
            {
                "nombre": "Beans - Kidney, Canned",
                "descripcion": "Maecenas tristique, est et tempus semper, est quam pharetra magna, ac consequat metus sapien ut nunc. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia Curae; Mauris viverra diam vitae quam. Suspendisse potenti.\n\nNullam porttitor lacus at turpis. Donec posuere metus vitae ipsum. Aliquam non mauris.",
                "precio": 492.05,
                "categoria": "Phone case",
                "inventario": 64,
                "sku": "ISNPS-SKU-503",
                "fecha_lanzamiento": "02/17/2025",
                "imagen_url": "https://ejemplo.com/szhc0.png",
                "id": "98d2ce3d-a416-4706-8d46-99e52e67bb2e"
            }
        ]
        nombre = "Beans - Kidney"
        expected_products_model = [models.Product.model_validate(p) for p in expected_products_json]

        # Act
        products = asyncio.run(app.read_products(nombre=nombre))
        

        # Assert
        self.assertEqual(len(products), expected_products_count)
        self.assertEqual(products, expected_products_model)

    def test_read_products_pricemin_filter(self):
        # Arrange
        expected_products_count = 2
        expected_products_json = [
            {
                "nombre": "Cup - 6oz, Foam",
                "descripcion": "Curabitur at ipsum ac tellus semper interdum. Mauris ullamcorper purus sit amet nulla. Quisque arcu libero, rutrum ac, lobortis vel, dapibus at, diam.",
                "precio": 996.76,
                "categoria": "Water bottle",
                "inventario": 75,
                "sku": "CMVEA-SKU-009",
                "fecha_lanzamiento": "01/23/2025",
                "imagen_url": "https://ejemplo.com/mp41y.png",
                "id": "64e0920f-3a95-4980-b047-59c1a206ad78"
            },
            {
                "nombre": "Cocoa Butter",
                "descripcion": "Curabitur gravida nisi at nibh. In hac habitasse platea dictumst. Aliquam augue quam, sollicitudin vitae, consectetuer eget, rutrum at, lorem.",
                "precio": 996.64,
                "categoria": "Water bottle",
                "inventario": 99,
                "sku": "IJKLA-SKU-069",
                "fecha_lanzamiento": "06/16/2025",
                "imagen_url": "https://ejemplo.com/qd0mp.png",
                "id": "aae3b0fd-534e-42db-bbe2-edaf703a9b55"
            }
        ]
        precio = 995.00
        expected_products_model = [models.Product.model_validate(p) for p in expected_products_json]

        # Act
        products = asyncio.run(app.read_products(precio_min=precio))
        

        # Assert
        self.assertEqual(len(products), expected_products_count)
        self.assertEqual(products, expected_products_model)

    def test_read_products_pricemax_filter(self):
        # Arrange
        expected_products_count = 6
        expected_products_json = [
            {
                "nombre": "Energy - Boo - Koo",
                "descripcion": "Cras mi pede, malesuada in, imperdiet et, commodo vulputate, justo. In blandit ultrices enim. Lorem ipsum dolor sit amet, consectetuer adipiscing elit.",
                "precio": 14.48,
                "categoria": "Phone case",
                "inventario": 30,
                "sku": "MKRMO-SKU-872",
                "fecha_lanzamiento": "03/12/2025",
                "imagen_url": "https://ejemplo.com/p8lk4.png",
                "id": "d6f69784-5e63-43e1-9fbe-3bfd00bc1cf5"
            },
            {
                "nombre": "Wine - Rioja Campo Viejo",
                "descripcion": "Nam ultrices, libero non mattis pulvinar, nulla pede ullamcorper augue, a suscipit nulla elit ac nulla. Sed vel enim sit amet nunc viverra dapibus. Nulla suscipit ligula in lacus.\n\nCurabitur at ipsum ac tellus semper interdum. Mauris ullamcorper purus sit amet nulla. Quisque arcu libero, rutrum ac, lobortis vel, dapibus at, diam.",
                "precio": 11.78,
                "categoria": "Phone case",
                "inventario": 17,
                "sku": "MZYDI-SKU-947",
                "fecha_lanzamiento": "11/01/2025",
                "imagen_url": "https://ejemplo.com/7530m.png",
                "id": "f98b1e3a-26f6-44f1-8e3b-e26475fb83b0"
            },
            {
                "nombre": "Dc - Sakura Fu",
                "descripcion": "Praesent blandit. Nam nulla. Integer pede justo, lacinia eget, tincidunt eget, tempus vel, pede.\n\nMorbi porttitor lorem id ligula. Suspendisse ornare consequat lectus. In est risus, auctor sed, tristique in, tempus sit amet, sem.",
                "precio": 12.12,
                "categoria": "Phone case",
                "inventario": 10,
                "sku": "HABCT-SKU-132",
                "fecha_lanzamiento": "01/25/2025",
                "imagen_url": "https://ejemplo.com/xu54e.png",
                "id": "9e6be5b2-69f7-4453-92fa-6c2724467980"
            },
            {
                "nombre": "Sauce - Demi Glace",
                "descripcion": "Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Proin risus. Praesent lectus.",
                "precio": 14.3,
                "categoria": "Notebook",
                "inventario": 70,
                "sku": "VJINO-SKU-009",
                "fecha_lanzamiento": "10/28/2025",
                "imagen_url": "https://ejemplo.com/ryc54.png",
                "id": "5b243420-dcd4-4fe0-9500-ebcdc2bb0d61"
            },
            {
                "nombre": "Chocolate - Chips Compound",
                "descripcion": "Fusce consequat. Nulla nisl. Nunc nisl.",
                "precio": 12.19,
                "categoria": "Phone case",
                "inventario": 1,
                "sku": "PYKOM-SKU-883",
                "fecha_lanzamiento": "04/24/2025",
                "imagen_url": "https://ejemplo.com/829ln.png",
                "id": "817e4cdb-c009-4368-8524-068f236eb447"
            },
            {
                "nombre": "Sponge Cake Mix - Vanilla",
                "descripcion": "Praesent blandit. Nam nulla. Integer pede justo, lacinia eget, tincidunt eget, tempus vel, pede.",
                "precio": 12.71,
                "categoria": "Phone case",
                "inventario": 57,
                "sku": "TAKSG-SKU-195",
                "fecha_lanzamiento": "12/05/2024",
                "imagen_url": "https://ejemplo.com/a81nt.png",
                "id": "e55071b3-3a6a-4738-b6a4-9a4507ca50bf"
            }
        ]
        precio = 15.00
        expected_products_model = [models.Product.model_validate(p) for p in expected_products_json]

        # Act
        products = asyncio.run(app.read_products(precio_max=precio))
        

        # Assert
        self.assertEqual(len(products), expected_products_count)
        self.assertEqual(products, expected_products_model)

    def test_read_products_category_filter(self):
        # Arrange
        expected_products_count = 1
        expected_products_json = [
            {
                "nombre": "Taro Leaves",
                "descripcion": "Suspendisse potenti. In eleifend quam a odio. In hac habitasse platea dictumst.",
                "precio": 608.24,
                "categoria": "Tarot",
                "inventario": 35,
                "sku": "ILQNG-SKU-428",
                "fecha_lanzamiento": "09/07/2025",
                "imagen_url": "https://ejemplo.com/76xbk.png",
                "id": "0e091c7f-9008-4afa-94cd-9afe8bbf6e4f"
            }
        ]
        categoria = "Tarot"
        expected_products_model = [models.Product.model_validate(p) for p in expected_products_json]

        # Act
        products = asyncio.run(app.read_products(categoria=categoria))
        

        # Assert
        self.assertEqual(len(products), expected_products_count)
        self.assertEqual(products, expected_products_model)

#4. Actualización de Producto (PUT /productos/{id}):
class TEST_4_Lectura_Producto_Específico(unittest.TestCase):
    def setUp(self):
        self.id = "cddf966f-2a1d-47fd-871a-bad6c7e408f9"
        self.original_Product = {"id":"cddf966f-2a1d-47fd-871a-bad6c7e408f9","nombre":"Pasta - Fusili, Dry","descripcion":"Pasta Penne","precio":284.54,"categoria":"Pasta","inventario":27,"sku":"UFWQP-SKU-891","fecha_lanzamiento":"05/23/2025","imagen_url":"https://ejemplo.com/at58h.png"}
        self.update_Product = {"nombre":"Pasta - Fusili, Dry","descripcion":"Pasta Penne de secado rapido","precio":15.50,"categoria":"Pasta","inventario":100,"sku":"PASTA-SKU-891","fecha_lanzamiento":"05/23/2000","imagen_url":"https://ejemplo.com/at58h.png"}
        current_dir = os.path.dirname(os.path.abspath(__file__))
        project_root = os.path.dirname(current_dir)
        app.PRODUCTS_FILE = str(project_root) + "\data\MOCK_DATA.json"
    def test_ejemplo(self):
        pass
        self.assertEqual(1,1)
        
    def test_Product_update(self):
        # Arrange
        update_product = SCHEMA.ProductUpdate(**self.update_Product)

        # Act
        data_saved = asyncio.run(app.update_product(self.id, update_product)).dict()
        self.update_Product["id"] = self.id
        
        # Assert
        self.assertEqual(self.update_Product["id"], data_saved["id"], 'Error El id no es igual')
        self.assertEqual(self.update_Product["nombre"], data_saved["nombre"])
        self.assertEqual(self.update_Product["descripcion"], data_saved["descripcion"])
        self.assertAlmostEqual(self.update_Product["precio"], data_saved["precio"])
        self.assertEqual(self.update_Product["categoria"], data_saved["categoria"])
        self.assertEqual(self.update_Product["inventario"], data_saved["inventario"])
        self.assertEqual(self.update_Product["sku"], data_saved["sku"])
        self.assertEqual(self.update_Product["fecha_lanzamiento"], data_saved["fecha_lanzamiento"].strftime("%m/%d/%Y"))
        self.assertEqual(self.update_Product["imagen_url"], data_saved["imagen_url"])




if __name__ == '__main__':
    unittest.main()