import requests
import sender_stand_request
import data

# esta función cambia los valores en el parámetro "name"
def get_kit_body(name):
    # el diccionario que contiene el cuerpo de solicitud se copia del archivo "data" (datos) para conservar los datos del diccionario de origen
    current_body = data.kit_body.copy()
    # Se cambia el valor del parámetro name
    current_body["name"] = name
    # Se devuelve un nuevo diccionario con el valor name requerido
    return current_body

def get_new_user_token():
    response = sender_stand_request.post_new_user(data.user_body)
    return response.json()["authToken"]

def positive_assert(kit_body):
    response = sender_stand_request.post_new_client_kit(kit_body, get_new_user_token())
    # Comprueba si el código de estado es 201
    assert response.status_code == 201
    assert response.json()["name"] == kit_body["name"]

def negative_assert(kit_body):
    response = sender_stand_request.post_new_client_kit(kit_body, get_new_user_token())
    assert response.status_code == 400


# Test 1: El número permitido de caracteres (1)
def test_1_crear_kit_con_1_caracter():
    new_kit_body = get_kit_body("a")
    positive_assert(new_kit_body)


# Test 2: El número permitido de caracteres (511)
def test_2_crear_kit_con_511_caracteres():
    # Valor de prueba específico de exactamente 511 caracteres
    name_511_chars = "AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabC"
    new_kit_body = get_kit_body(name_511_chars)
    positive_assert(new_kit_body)


# Test 3: El número de caracteres es menor que la cantidad permitida (0)
def test_3_crear_kit_con_0_caracteres():
    new_kit_body = get_kit_body("")
    negative_assert(new_kit_body)


# Test 4: El número de caracteres es mayor que la cantidad permitida (512)
def test_4_crear_kit_con_512_caracteres():
    # Valor de prueba específico de exactamente 512 caracteres
    name_512_chars = "AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcD"
    new_kit_body = get_kit_body(name_512_chars)
    negative_assert(new_kit_body)


# Test 5: Se permiten caracteres especiales
def test_5_crear_kit_con_caracteres_especiales():
    new_kit_body = get_kit_body("№%@,")
    positive_assert(new_kit_body)


# Test 6: Se permiten espacios
def test_6_crear_kit_con_espacios():
    new_kit_body = get_kit_body(" A Aaa ")
    positive_assert(new_kit_body)


# Test 7: Se permiten números
def test_7_crear_kit_con_numeros():
    new_kit_body = get_kit_body("123")
    positive_assert(new_kit_body)


# Test 8: El parámetro no se pasa en la solicitud
def test_8_crear_kit_sin_parametro_name():
    # Crear un cuerpo de solicitud sin el parámetro "name"
    kit_body = data.kit_body.copy()
    if "name" in kit_body:
        del kit_body["name"]
    response = sender_stand_request.post_new_client_kit(kit_body, get_new_user_token())
    assert response.status_code == 400


# Test 9: Se ha pasado un tipo de parámetro diferente (número)
def test_9_crear_kit_con_tipo_numero():
    # Crear un cuerpo de solicitud donde "name" es un número en lugar de string
    kit_body = data.kit_body.copy()
    kit_body["name"] = 123
    response = sender_stand_request.post_new_client_kit(kit_body, get_new_user_token())
    assert response.status_code == 400


