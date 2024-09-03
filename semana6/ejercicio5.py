def busqueda_letras():
  mayusculas=0
  minusculas=0
  texto = "I love Nacion Sushi"
  for i in texto: 
    if i.isupper()==True:
      mayusculas+=1
    elif i.islower(): 
      minusculas+=1
  print(f"Mayusculas {mayusculas} y {minusculas} minusculas ")


busqueda_letras()