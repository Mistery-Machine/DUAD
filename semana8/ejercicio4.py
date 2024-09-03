import csv

archivo_juego='lista_juegos.csv'

def definir_juegos(n):
  juegos=[]
  for i in range(n):
    nombre=input("Ingrese el nombre del juego: ")
    genero=input("Ingrese el genero del juego: ")
    desarrollador=input("Ingrese el desarrollador: ") 
    clasificacion=input("Cual es la clasificacion del juego?: ")
    juegos.append([nombre,genero,desarrollador,clasificacion])
  return juegos 

def crear_csv(juego,archivo_juego):
  with open(archivo_juego, 'w') as file: 
    
    escribir_csv=csv.writer(file, delimiter='\t')
    escribir_csv.writerow(["Nombre","Genero","desarrollador","clasificacion"])
    for i in juego: 
      escribir_csv.writerow(i)
      
def main():
  n = int(input("Cuantos juegos quiere ingresar?: "))
  juegos = definir_juegos (n)
  crear_csv(juegos, archivo_juego)

if __name__ == "__main__":
  main()
