import csv
import logic


class Student:
    def __init__(self, name, classroom, spanish_note, english_note, soc_studies_note, science_note):
        self.name = name
        self.classroom = classroom
        self.spanish_note = spanish_note
        self.english_note = english_note
        self.soc_studies_note = soc_studies_note
        self.science_note = science_note

    @property
    def average(self):
        return (self.spanish_note + self.english_note + self.soc_studies_note + self.science_note) / 4

    def to_dict(self):
        return {
            'name': self.name,
            'classroom': self.classroom,
            'spanish_note': self.spanish_note,
            'english_note': self.english_note,
            'soc_studies_note': self.soc_studies_note,
            'science_note': self.science_note,
            'average': self.average
        }


def export_data(students, filename="csv_file.csv"):
    headers = ["Name", "Classroom", "Spanish", "English", "Soc Studies", "Science", "Average"]

    with open(filename, mode="a", newline="") as file:
        writer = csv.writer(file)
        if file.tell() == 0:
            writer.writerow(headers)

        for student in students:
            row = [
                student.name,
                student.classroom,
                student.spanish_note,
                student.english_note,
                student.soc_studies_note,
                student.science_note,
                student.average  
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
                
                if len(row) == 6: 
                    try:
                        student = Student(
                            name=row[0],
                            classroom=row[1],
                            spanish_note=int(row[2]),
                            english_note=int(row[3]),
                            soc_studies_note=int(row[4]),
                            science_note=int(row[5])
                        )
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