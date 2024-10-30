from menu import result
from logic import registering_students, average_notes, calculate_top_three, overall_average, display_students
from data import export_data, import_data 

def main():
    print("---- Welcome to the Student Management System! ---- ")

    registered_students = []
    averages = {}
    overall_avg = 0

    while True:
        try:
            student_amount = int(input("Enter the number of students you want to register: "))
            if student_amount < 0:
                print("El número de estudiantes no puede ser negativo.")
            else:
                break
        except ValueError:
            print("Por favor, ingrese un número válido.")

    if student_amount > 0:
        registered_students = registering_students(student_amount)
        averages = average_notes(registered_students)
        overall_avg = overall_average(averages)
    else:
        print("No se registraron estudiantes.")
    display_students(registered_students)
    export_data(registered_students)
    result(registered_students, averages, overall_avg)

if __name__ == "__main__":
    main()