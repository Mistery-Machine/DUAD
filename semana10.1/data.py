import csv 
import logic


def export_data(students, averages, total_average, filename="csv_file.csv"):
  headers = ["Name", "Classroom", "Spanish", "English", "Soc Studies", "Science", "Average", "Total average"]

  with open (filename, mode ="w", newline="") as file: 
    writer = csv.writer(file)
    writer.writerow(headers)

    for student, avg in zip(students, averages):
      row = [
        student['name'],
        student['classroom'],
        student['spanish_note'],
        student['english_note'],
        student['soc_studies_note'],
        student['science_note'],
        avg  
            ]
      writer.writerow(row)
    writer.writerow(["", "", "", "", "", "Class Average", total_average])



def import_data(csv_file):
  students = []
  try: 
    with open("csv_file.csv", mode='r', newline='') as file:
      read_csv = csv.reader(csv_file)

      for row in read_csv:
        if len(row) > 6 and row[0]:
          student = {
            'name': row[0],
            'classroom':row[1],
            'spanish_note':int(row[2]),
            'english_note':int(row[3]),
            'soc_studies_note':int(row[4]),
            'science_note':int(row[5]),
            'average':int(row[6])
          }

          students.append(student)
      print("File loaded succesfully")
      return students
  except FileNotFoundError:
    print("File does not exist")