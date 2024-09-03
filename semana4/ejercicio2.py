nombre = input("Ingrese su nombre: ")
apellido = input("Ingrese su apellido: ")
edad =int(input("Ingrese su edad en anios: "))

if (edad >=65):
  estado="adulto mayor"
elif (edad >=35):
  estado = "adulto"
elif (edad >=18):
  estado = "adulto joven"
elif (edad >=12):
  estado = "adolescente"
elif (edad >=10):
  estado = "preadolescente"
elif (edad >=3):
  estado = "nino"
elif (edad >=0):
  estado = "bebe"

print(f"Su nombre es {nombre} {apellido} y usted es un {estado}")