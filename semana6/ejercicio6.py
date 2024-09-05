def orden_alfabetico():
  oracion = "python-variable-funcion-computadora-monitor"
  lista = oracion.split("-")
  lista.sort()
  str = "-".join(lista)
  print(str)


orden_alfabetico()