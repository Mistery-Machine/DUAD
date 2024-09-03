def menu():
    print("*** Menu Principal ***")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicacion")
    print("4. Division")
    print("5. Borrar resultado")
    print("6. Salir")

def calculadora():
    resultado = 0

    while True:
        print(f"Numero actual: {resultado}")
        menu()
        while True:
            try:
                opcion = int(input("Ingrese el numero de la operacion: "))
                if opcion not in range(1, 7):
                    print("Ingrese un numero correcto entre 1 y 6")
                else:
                    break
            except ValueError:
                print("Ingrese un numero correcto entre 1 y 6")

        if opcion == 6:
            print("Muchas gracias")
            break

        if opcion in [1, 2, 3, 4]:
            while True:
                try:
                    numero = int(input("Ingrese el numero: "))
                    break
                except ValueError:
                    print("Por favor digite numeros solamente")

            if opcion == 1:
                resultado += numero
            elif opcion == 2:
                resultado -= numero
            elif opcion == 3:
                resultado *= numero
            elif opcion == 4:
                if numero != 0:
                    resultado //= numero
                else:
                    print("No se puede dividir por cero")
                    continue
        elif opcion == 5:
            resultado = 0
            print("Resultado borrado.")

        print(f"Resultado: {resultado}")

if __name__ == "__main__":
    calculadora()