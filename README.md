Mauricio López

Walter Villatoro

Mario Armas

Esteban Ruiz

Dulce García

# API de Catálogo de Productos

Este proyecto implementa una API RESTful para gestionar un catálogo de productos utilizando FastAPI y almacenamiento en JSON.

El proyecto esta contenido en ``./APP``

## 1. Inicialización del Proyecto

Existen dos forma de inicialización del Proyecto

### 1. Inicialización con terminal
Sigue estos pasos para inicializar el proyecto:

1. Clona el repositorio:
   ```
   git clone https://github.com/tu-usuario/api-catalogo-productos.git
   cd api-catalogo-productos
   ```

2. Crea un entorno virtual e instala las dependencias:
   ```
   python -m venv venv
   source venv/bin/activate  # En Windows usa: venv\Scripts\activate
   pip install -r requirements.txt
   ```

3. Inicia el servidor de desarrollo:
   ```
   uvicorn app.main:app --reload
   ```

### 2. Con VS Code 

1. Ir clonar el repositorio
   ```
   git clone https://github.com/tu-usuario/api-catalogo-productos.git
   cd api-catalogo-productos
   ```

2. ir a la secion de debug
    ```
    CTRL+SHIFT+D
    ```

3. Seleccionar FastAPI main.py
    ```
    recionar F5
    ```

La API estará disponible en `http://localhost:8000`.

## 2. Funcionamiento de la API

La API proporciona los siguientes endpoints:

### Crear Producto (POST /productos)
- Crea un nuevo producto en el catálogo.
- Ejemplo de uso:
  ```
  curl -X POST "http://localhost:8000/productos" -H "Content-Type: application/json" -d '{"nombre":"Producto Nuevo","precio":99.99,"categoria":"Electrónica","inventario":10,"sku":"PROD-001"}'
  ```

### Obtener Todos los Productos (GET /productos)
- Retorna todos los productos en el catálogo.
- Soporta filtrado por nombre, categoría y rango de precios.
- Ejemplo de uso:
  ```
  curl "http://localhost:8000/productos?categoria=Electrónica&precio_min=50&precio_max=200"
  ```

### Obtener un Producto Específico (GET /productos/{id})
- Retorna un producto específico por su ID o SKU.
- Ejemplo de uso:
  ```
  curl "http://localhost:8000/productos/PROD-001"
  ```

### Actualizar Producto (PUT /productos/{id})
- Actualiza los detalles de un producto específico.
- Ejemplo de uso:
  ```
  curl -X PUT "http://localhost:8000/productos/PROD-001" -H "Content-Type: application/json" -d '{"precio":89.99,"inventario":15}'
  ```

### Eliminar Producto (DELETE /productos/{id})
- Elimina un producto específico del catálogo.
- Ejemplo de uso:
  ```
  curl -X DELETE "http://localhost:8000/productos/PROD-001"
  ```

## 3. Estructura de Datos y Modelos

### Modelo de Producto

Los productos se representan con la siguiente estructura:

```python
{
    "id": str,  # UUID generado automáticamente
    "nombre": str,  # 3-100 caracteres
    "descripcion": Optional[str],  # Máximo 500 caracteres
    "precio": float,  # Número positivo con máximo 2 decimales
    "categoria": str,  # De una lista predefinida
    "inventario": int,  # Número entero no negativo
    "sku": str,  # 6-20 caracteres, único
    "fecha_lanzamiento": Optional[date],  # Formato YYYY-MM-DD
    "imagen_url": Optional[str]  # URL válida
}
```

### Almacenamiento de Datos

Los productos se almacenan en un archivo JSON (`data/productos.json`). Cada entrada en el archivo representa un producto con la estructura descrita anteriormente.

## 4. Información Adicional

### Documentación de la API
- Accede a la documentación interactiva de la API en `http://localhost:8000/docs`
- Para una versión alternativa de la documentación, visita `http://localhost:8000/redoc`

### Pruebas
Para ejecutar las pruebas unitarias:
```
python -m unittest discover tests
```

### Contribuciones
Las contribuciones son bienvenidas. Por favor, asegúrate de actualizar las pruebas según sea necesario.

## 5. Creadores del Proyecto

Este proyecto fue desarrollado por:

1. Mauricio Lopez. Carne: 1270818
2. Mario Armas. Carne: 1093721
3. [Nombre del Creador 3]
4. [Nombre del Creador 4]
5. [Nombre del Creador 5]

---

Para más información o soporte, por favor abre un issue en el repositorio del proyecto.
