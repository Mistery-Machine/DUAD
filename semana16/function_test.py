la_lista = [4, 6, 2, 29]

def suma_numeros (la_lista):
  suma=0
  for i in la_lista: 
    suma+=i
  return(suma)
  

resultado = suma_numeros(la_lista)
print("La suma total es:", resultado)


def primera_funcion(my_string):
  resultado=""
  for i in reversed(my_string):
    resultado+=i
  return resultado
  




def busqueda_letras(texto):
  mayusculas=0
  minusculas=0
  for i in texto: 
    if i.isupper()==True:
      mayusculas+=1
    elif i.islower(): 
      minusculas+=1
  return mayusculas, minusculas


