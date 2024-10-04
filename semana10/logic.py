def correct_notes(subject):
  while True:
    try: 
      grade= int(input(f"Enter the score in {subject}:  "))
      if 0 <= grade <=100:
        return grade
      else: 
        print("Enter values between 0 and 100")
    except ValueError: 
      print("Invalid Input, please enter a number")

def registering_students(n): 
  students = []

  for i in range(n):
    name= input("Enter students name: ")
    classroom = input("Enter the classoroom ID student is cursing: ")
    spanish_note= correct_notes("Spanish")
    english_note= correct_notes("English")
    soc_studies_note= correct_notes("Soc Studies")
    science_note= correct_notes("Science")

    studen_info={
      "name":name,
      "classroom":classroom,
      "spanish_note":spanish_note,
      "english_note":english_note,
      "soc_studies_note":soc_studies_note,
      "science_note":science_note
    }
    students.append(studen_info)

  return students


def average_notes(students): 
  averages={}
  for student in students: 
    name = student["name"]
    grades = [
      student["spanish_note"],
      student["english_note"],
      student["soc_studies_note"],
      student["science_note"]
      ]
  average = sum(grades)/ len(grades)
  averages[name]=average
  return averages

def calculate_top_three(averages):

  sorted_averages = sorted(averages.items(), key=lambda x: x[1],  reverse = True)
  top_three = sorted_averages [:3]
  return top_three


def overall_average(averages): 
  total_average= sum(averages.values())/len(averages) if averages else 0
  return total_average


#Display functions 

def display_students(students): 
  print("-- List of registered students --")
  for i, student  in enumerate(students, start=1):
    print(f"\nStudent {i}:")
    print(f"Name: {student['name']}")
    print(f"Classroom: {student['classroom']}")
    print(f"Spanish Note: {student['spanish_note']}")
    print(f"English Note: {student['english_note']}")
    print(f"Social Studies Note: {student['soc_studies_note']}")
    print(f"Science Note: {student['science_note']}")

def top_three(top_3_students): 
  for i, (name, average) in enumerate(top_3_students, start=1): 
    print(f"{i}. {name} with average {average}")

def print_overall_average(averages):
  average = overall_average(averages)
  print(f"The overage score is {average} ")




    





  







 



    
  





