list_a = ["first_name", "last_name", "role"]
list_b = ["Alek", "Castillo", "Software Engineer"]

diccionario = {list_a[i]: list_b[i] for i in range(len(list_a))}
print(diccionario)