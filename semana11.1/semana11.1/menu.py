from logic import display_students, top_three, print_overall_average, calculate_top_three, average_notes, overall_average
from data import import_data, export_data
from data import Student  

def menu():
    print("*** Menu Principal ***")
    print("1. View all students ")
    print("2. View Top 3 best students ")
    print("3. View overall average notes ")
    print("4. Export data to a CSV file  ")
    print("5. Import data from the CSV file ")
    print("6. Log out ")

def result(students, averages, overall_avg): 
    while True:
        menu()
        try:
            option = int(input("Enter the number of the action you want to perform: "))
            if option not in range(1, 7):
                print("Enter a correct number between 1 and 6")
                continue  
        except ValueError:
            print("Enter a correct number between 1 and 6")
            continue

        if option == 6:
            print("Logged out successfully.")
            break
        
        if option == 1:
            if students:
                display_students(students)
            else:
                print("There's no students registered.")
                
        elif option == 2:
            if averages:
                top_3_students = calculate_top_three(averages)
                top_three(top_3_students)
            else:
                print("There's no averages to calculate.")
        
        elif option == 3:
            if averages:
                print_overall_average(averages)
            else:
                print("There's no averages available.")
                
        elif option == 4:
            if students and averages:
                total_avg = overall_average(averages)
                export_data(students)  
                print("Data exported successfully.")
            else:
                print("There's no data to export.")
                  
        elif option == 5:
            imported_students = import_data("csv_file.csv")
            if imported_students:
                
                for student_data in imported_students:
                    student = Student(
                        name=student_data['name'],
                        classroom=student_data['classroom'],
                        spanish_note=student_data['spanish_note'],
                        english_note=student_data['english_note'],
                        soc_studies_note=student_data['soc_studies_note'],
                        science_note=student_data['science_note']
                    )
                    students.append(student)  
                print("Students imported successfully.")
            else:
                print("No students were imported.")