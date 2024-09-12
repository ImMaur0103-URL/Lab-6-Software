from fastapi import FastAPI, HTTPException, Query
from typing import List, Optional
from schemas import ProductCreate, ProductUpdate, ProductResponse
from models import Product
from utils import load_products, save_products
# Inicialización de la API con FastAPI
app = FastAPI()

# Ruta POST para crear un nuevo producto
@app.post("/productos", response_model=ProductResponse)
async def create_product(product: ProductCreate):
    products = load_products()
    new_product = Product(**product.dict())
    if any(p.sku == new_product.sku for p in products):
        raise HTTPException(status_code=400, detail="SKU ya existe")
    products.append(new_product)
    save_products(products)
    return new_product

# Ruta GET para obtener todos los productos, filtrados por nombre, categoría, precio mínimo y precio máximo
@app.get("/productos", response_model=List[ProductResponse])
async def read_products(
    nombre: Optional[str] = None,
    categoria: Optional[str] = None,
    precio_min: Optional[float] = None,
    precio_max: Optional[float] = None
):
    products = load_products()
    if nombre:
        products = [p for p in products if nombre.lower() in p.nombre.lower()]
    if categoria:
        products = [p for p in products if p.categoria == categoria]
    if precio_min is not None:
        products = [p for p in products if p.precio >= precio_min]
    if precio_max is not None:
        products = [p for p in products if p.precio <= precio_max]
    return products

# Ruta GET para obtener un producto específico por ID o SKU
@app.get("/productos/{product_id}", response_model=ProductResponse)
async def read_product(product_id: str):
    products = load_products()
    product = next((p for p in products if p.id == product_id or p.sku == product_id), None)
    if product is None:
        raise HTTPException(status_code=404, detail="Producto no encontrado")
    return product

# Ruta PUT para actualizar un producto específico por ID
@app.put("/productos/{product_id}", response_model=ProductResponse)
async def update_product(product_id: str, product_update: ProductUpdate):
    products = load_products()
    product_index = next((i for i, p in enumerate(products) if p.id == product_id), None)
    if product_index is None:
        raise HTTPException(status_code=404, detail="Producto no encontrado")
    
    updated_product = products[product_index].copy(update=product_update.dict(exclude_unset=True))
    products[product_index] = updated_product
    save_products(products)
    return updated_product

# Ruta DELETE para eliminar un producto específico por ID
@app.delete("/productos/{product_id}", response_model=dict)
async def delete_product(product_id: str):
    products = load_products()
    product_index = next((i for i, p in enumerate(products) if p.id == product_id), None)
    if product_index is None:
        raise HTTPException(status_code=404, detail="Producto no encontrado")
    
    del products[product_index]
    save_products(products)
    return {"message": "Producto eliminado exitosamente"}

