from logic import display_students, top_three, print_overall_average, calculate_top_three, average_notes,overall_average
from data import import_data, export_data
import data

def menu():
    print("*** Menu Principal ***")
    print("1.View all students ")
    print("2.View Top 3 best students ")
    print("3.View overall average notes ")
    print("4.Export data to a CSV file  ")
    print("5.Import data from the CSV file ")
    print("6.Log out ")

def result (students, averages): 
    while True:
        menu()
        while True:
            try:
                option = int(input("Enter the number of the action you want to perform: "))
                if option not in range(1, 7):
                    print("Enter a correct number between 1 y 6")
                else:
                    break
            except ValueError:
                print("Enter a correct number between 1 y 6")

        if option == 6:
            print("Logged out succesfully.")
            break

        if option == 1:
            display_students(students)
                
        elif option == 2:
            top_3_students = calculate_top_three(averages)
            top_three(top_3_students)
                
        elif option == 3:
            print_overall_average(averages)
                
        elif option == 4:
            total_avg = overall_average(averages)
            export_data(students, averages, total_avg)
                  
        elif option == 5:
            imported_students = import_data("csv_file.csv")
            if imported_students:
                students.extend(imported_students)
                print("Students imported successfully.")
