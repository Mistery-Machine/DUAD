import random

numero_ingreso = int(input("Ingrese un numero del 1 al 10: "))
numero_random = random.randint(1,10)
while (numero_ingreso != numero_random):
  numero_ingreso =int(input("Ingrese otro numero: "))

print(f"El numero secreto es {numero_ingreso}")