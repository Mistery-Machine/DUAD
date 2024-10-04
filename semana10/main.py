from menu import result
from logic import registering_students, average_notes, calculate_top_three, display_students
from data import export_data, import_data

def main():
  print("---- Welcome to the Student Management System! ---- ")

  student_ammount= int(input("Enter the number of students you want to register: "))
  registered_students= registering_students(student_ammount)
  averages = average_notes(registered_students)

  result(registered_students, averages)

if __name__ == "__main__":
    main()