lista = []

for i in range(10):
  numero= int(input("Ingrese un numero: "))
  lista.append(numero)
  max_num = max(lista)

print(f"{lista} El numero maximo es: {max_num}")