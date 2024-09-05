ruta_de_canciones = "canciones.txt"
destino= "nuevas_canciones.txt"

def leer_canciones(ruta): 
  contenido=[]
  with open (ruta, 'r') as file: 
    for i in file.readlines():
      contenido.append(i)
    return contenido


def escribir_canciones(destino, contenido):
  with open(destino,'w')as file: 
    for linea in sorted(contenido):
      file.write(linea)


if __name__ == "__main__":
  contenido = leer_canciones(ruta_de_canciones)
  escribir_canciones(destino, contenido)