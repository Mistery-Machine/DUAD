diccionario = {"name": "John", "email": "john@ecorp.com", "access_level": 5, "age": 28}
keys_eliminados = ["access_level", "age"]

for i in keys_eliminados:
    diccionario.pop(i, None)

print(diccionario)