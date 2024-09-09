# tests/test_main.py
from fastapi.testclient import TestClient
from app.main import app
from app.utils import load_products, save_products

client = TestClient(app)

def test_create_product():
    # Guardar los productos actuales
    original_products = load_products()

    # Datos del nuevo producto
    new_product = {
        "nombre": "Producto de prueba",
        "descripcion": "Este es un producto de prueba",
        "precio": 99.99,
        "categoria": "Electrónica",
        "inventario": 10,
        "sku": "TEST-SKU-001"
    }

    # Enviar solicitud POST para crear el producto
    response = client.post("/productos", json=new_product)

    # Verificar que la respuesta sea exitosa
    assert response.status_code == 200

    # Verificar que el producto se haya creado correctamente
    created_product = response.json()
    assert created_product["nombre"] == new_product["nombre"]
    assert created_product["sku"] == new_product["sku"]

    # Verificar que el producto se haya guardado en el archivo JSON
    updated_products = load_products()
    assert len(updated_products) == len(original_products) + 1

    # Restaurar los productos originales
    save_products(original_products)

# Ejecutar las pruebas con: pytest tests/test_main.py