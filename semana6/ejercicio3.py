la_lista = [4, 6, 2, 29]

def suma_numeros (la_lista):
  suma=0
  for i in la_lista: 
    suma+=i
  return(suma)
  

resultado = suma_numeros(la_lista)
print("La suma total es:", resultado)