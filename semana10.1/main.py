from menu import result
from logic import registering_students, average_notes, calculate_top_three, display_students
from data import export_data, import_data

def main():
    print("---- Welcome to the Student Management System! ---- ")

    while True:
        try:
            student_amount = int(input("Enter the number of students you want to register: "))
            if student_amount <= 0:
                print("El número de estudiantes no puede ser negativo.")
            else:
                break
        except ValueError:
            print("Por favor, ingrese un número válido.")

    # Si se ingresan estudiantes válidos
    if student_amount > 0:
        registered_students = registering_students(student_amount)
        averages = average_notes(registered_students)
       
    else:
        # Si no se registran estudiantes
        registered_students = []
        averages = {}
        overall_avg = 0
        print("No se registraron estudiantes.")

    # Ejecutar las demás opciones del programa
    result(registered_students, averages, overall_avg)

if __name__ == "__main__":
    main()