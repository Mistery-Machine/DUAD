cantidad_notas=int(input("Ingrese la cantidad de notas a calcular: "))
contador = 1
cantidad_aprobadas=0
cantidad_desaprobadas=0
promedio_total=0
promedio_aprobadas=0
promedio_desaprobadas=0


while contador <= cantidad_notas:
  nota=int(input(f"Ingrese la nota numero {contador}: "))
  contador = contador+1
  if nota >=70: 
    cantidad_aprobadas = cantidad_aprobadas+1
    promedio_aprobadas = promedio_aprobadas + nota
  else:
    cantidad_desaprobadas = cantidad_desaprobadas+1
    promedio_desaprobadas = promedio_desaprobadas+1
  promedio_total=promedio_total+nota
  
promedio_total=promedio_total/3
promedio_aprobadas=promedio_aprobadas/cantidad_aprobadas
promedio_desaprobadas=promedio_desaprobadas/cantidad_desaprobadas

print(f"Su cantidad de notas aprobadas fue {cantidad_aprobadas}")
print(f"Su cantidad de notas aprobadas fue {cantidad_desaprobadas}")
print(f"Su cantidad de notas aprobadas fue {promedio_aprobadas}")
print(f"Su cantidad de notas aprobadas fue {promedio_desaprobadas}")
print(f"Su cantidad de notas aprobadas fue {promedio_total}")