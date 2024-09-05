import json
ruta_archivo="pokemones.json"
def leer_archivo_json(ruta):
  with open(ruta, 'r') as file: 
    return json.load(file)

def informacion_pokemon(): 
  nombre=input("Ingrese el nombre del nuevo pokemon: ")
  tipo=input("Ingrese el tipo: ")
  estadisticas_base = {
    "HP":int(input("HP:")),
    "Ataque":int(input("Ataque:")),
    "Defensa":int(input("Defensa:")),
    "Ataque Especial":int(input("Ataque Especial:")),
    "Defensa Especial":int(input("Defensa Especial:")),
    "Velocidad":int(input("Velocidad:"))
  }
  return{"Nombre":nombre,
         "Tipo":tipo,
         "Estadisticas base":estadisticas_base
  }

def inscribir_pokemon(pokemon_info):
  pokemones=leer_archivo_json(ruta_archivo)
  pokemones.append(pokemon_info)

  with open(ruta_archivo, "w") as file: 
    json.dump(pokemones,file, indent=4 )

def main(): 
    pokemon_info = informacion_pokemon()  
    inscribir_pokemon(pokemon_info)


if __name__ == "__main__":
  main()