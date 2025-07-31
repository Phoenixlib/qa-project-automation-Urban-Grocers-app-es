# Proyecto Urban Grocers 
# Pruebas de Validación de Kits

Este documento describe las pruebas automatizadas para la validación del campo `name` en la creación de kits de cliente.

## 📋 Descripción General

El conjunto de pruebas valida el comportamiento del endpoint de creación de kits de cliente, específicamente las reglas de validación para el campo `name`. Las pruebas cubren casos positivos (que deben funcionar) y casos negativos (que deben fallar con código de error 400).

## 🏗️ Estructura del Proyecto

```
proyecto/
├── test_kit_validation.py    # Archivo principal de pruebas
├── sender_stand_request.py   # Módulo para enviar solicitudes HTTP
├── data.py                   # Datos de configuración y cuerpos de solicitud
└── README.md                 # Este archivo
```

## 🧪 Lista de Pruebas

| N° | Descripción | Tipo | Código Esperado | Valor de Prueba |
|----|-------------|------|-----------------|-----------------|
| 1 | Número permitido de caracteres (1) | ✅ Positiva | 201 | `"a"` |
| 2 | Número permitido de caracteres (511) | ✅ Positiva | 201 | String de 511 caracteres |
| 3 | Número menor que permitido (0) | ❌ Negativa | 400 | `""` (string vacío) |
| 4 | Número mayor que permitido (512) | ❌ Negativa | 400 | String de 512 caracteres |
| 5 | Caracteres especiales permitidos | ✅ Positiva | 201 | `"№%@,"` |
| 6 | Espacios permitidos | ✅ Positiva | 201 | `" A Aaa "` |
| 7 | Números permitidos | ✅ Positiva | 201 | `"123"` |
| 8 | Parámetro faltante | ❌ Negativa | 400 | Sin campo `name` |
| 9 | Tipo de dato incorrecto | ❌ Negativa | 400 | `123` (número) |

## 🚀 Instalación y Configuración

### Prerrequisitos

- Python 3.7 o superior
- Biblioteca `requests`

### Instalación

```bash
# Instalar dependencias
pip install requests

# Clonar o descargar los archivos del proyecto
```

### Configuración

Asegúrate de que los siguientes archivos estén configurados correctamente:

**`data.py`** - Debe contener:
```python
# Cuerpo base para crear kits
kit_body = {
    "name": "Kit de prueba"
}

# Cuerpo para crear usuarios
user_body = {
    # ... configuración del usuario
}
```

**`sender_stand_request.py`** - Debe contener las funciones:
```python
def post_new_user(body):
    # Función para crear nuevos usuarios
    pass

def post_new_client_kit(body, token):
    # Función para crear kits de cliente
    pass
```

## 🏃‍♂️ Ejecución de Pruebas

### Ejecutar Todas las Pruebas

```bash
python test_kit_validation.py
```

### Ejecutar Pruebas Individuales

#### Con pytest (recomendado)
```bash
# Instalar pytest
pip install pytest

# Ejecutar todas las pruebas
pytest test_kit_validation.py -v

# Ejecutar una prueba específica
pytest test_kit_validation.py::test_1_crear_kit_con_1_caracter -v
```

#### Con unittest
```bash
# Ejecutar una prueba específica
python -c "import test_kit_validation; test_kit_validation.test_1_crear_kit_con_1_caracter()"
```

## 📊 Interpretación de Resultados

### Pruebas Exitosas
- **Código 201**: Para pruebas positivas, indica que el kit se creó correctamente
- **Código 400**: Para pruebas negativas, indica que la validación funciona correctamente

### Ejemplo de Salida
```
✅ test_1_crear_kit_con_1_caracter - PASSED
✅ test_2_crear_kit_con_511_caracteres - PASSED
✅ test_3_crear_kit_con_0_caracteres - PASSED
❌ test_4_crear_kit_con_512_caracteres - FAILED: AssertionError
...
📊 Resumen: 8 passed, 1 failed
```

## 🔧 Funciones Principales

### `get_kit_body(name)`
Crea un cuerpo de solicitud con el valor `name` especificado.

### `get_new_user_token()`
Obtiene un token de autorización creando un nuevo usuario.

### `positive_assert(kit_body)`
Valida respuestas exitosas (código 201) y verifica que el campo `name` coincida.

### `negative_assert(kit_body)`
Valida respuestas de error (código 400).

## 🐛 Resolución de Problemas

### Errores Comunes

**Error de conexión**
```
ConnectionError: Failed to establish connection
```
- Verificar que el servidor esté ejecutándose
- Confirmar la URL del endpoint

**Error de autenticación**
```
401 Unauthorized
```
- Verificar que la función `get_new_user_token()` funcione correctamente
- Confirmar que los datos del usuario sean válidos

**Error de importación**
```
ModuleNotFoundError: No module named 'sender_stand_request'
```
- Verificar que todos los archivos estén en el mismo directorio
- Confirmar que `sender_stand_request.py` y `data.py` existan

## 📝 Reglas de Validación del Campo `name`

### ✅ Valores Permitidos
- **Longitud**: 1-511 caracteres
- **Caracteres especiales**: №, %, @, comas, etc.
- **Espacios**: Al inicio, final y en medio
- **Números**: Como contenido del string
- **Letras**: Mayúsculas y minúsculas

### ❌ Valores No Permitidos
- **String vacío**: 0 caracteres
- **Muy largo**: Más de 511 caracteres
- **Tipo incorrecto**: Números, booleanos, objetos
- **Campo faltante**: No incluir el parámetro `name`

## 🤝 Contribución

Para agregar nuevas pruebas:

1. Crear una nueva función de prueba siguiendo el patrón `test_N_descripcion()`
2. Usar `positive_assert()` para casos que deben funcionar
3. Usar `negative_assert()` para casos que deben fallar
4. Agregar la nueva función a `run_all_tests()`
5. Actualizar esta documentación

## 📚 Referencias

- **Documentación de la API**: https://cnt-ae5572d0-666b-4dc2-a723-5babfa375910.containerhub.tripleten-services.com/docs/
- [Documentación de Requests](https://docs.python-requests.org/)
- [Guía de pytest](https://docs.pytest.org/)
- [Buenas prácticas de testing en Python](https://realpython.com/python-testing/)

---