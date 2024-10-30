import csv 
import logic


def export_data(students, averages, total_average, filename="csv_file.csv"):
  headers = ["Name", "Classroom", "Spanish", "English", "Soc Studies", "Science", "Average", "Total average"]

  with open (filename, mode ="a", newline="") as file: 
    writer = csv.writer(file)
    if file.tell()==0:
      writer.writerow(headers)

      for student in students:
            
            avg = (
                student['spanish_note'] +
                student['english_note'] +
                student['soc_studies_note'] +
                student['science_note']
            ) / 4  
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
    



def import_data(csv_file):
    students = []
    try:
        with open(csv_file, mode='r', newline='') as file_to_read:
            read_csv = csv.reader(file_to_read)
            next(read_csv)  
            for row in read_csv:
                print(f"Processing row: {row}")  
                
                if not row[0] or "Class Average" in row:
                    continue
                
                if len(row) == 7: 
                    try:
                        student = {
                            'name': row[0],
                            'classroom': row[1],
                            'spanish_note': int(row[2]),
                            'english_note': int(row[3]),
                            'soc_studies_note': int(row[4]),
                            'science_note': int(row[5]),
                            'average': float(row[6])  
                        }
                        students.append(student)
                    except ValueError:
                        print(f"Skipping invalid row due to ValueError: {row}")
                        continue
                else:
                    print(f"Skipping row with invalid length: {row}")

        if students:
            print("File loaded successfully")
        else:
            print("No students were imported.")
        return students

    except FileNotFoundError:
        print("File does not exist")