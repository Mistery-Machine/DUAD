from logic import display_students, top_three, print_overall_average, calculate_top_three, average_notes, overall_average
from data import import_data, export_data

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
                print("Enter a correct number between 1 y 6")
                continue  
        except ValueError:
            print("Enter a correct number between 1 y 6")
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
                export_data(students, averages, total_avg)
                print("Data exported succesfully.")
            else:
                print("There's no data to export.")
                  

        elif option == 5:
            imported_students = import_data("csv_file.csv")
            if imported_students:
                
                for student in imported_students:
                    if student not in students:
                        students.append(student)
                print("Students imported successfully.")
            else:
                print("No students were imported.")
