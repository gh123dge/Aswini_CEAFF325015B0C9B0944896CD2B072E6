class Students:

  def __init__(self, name, roll_number, cgpa):
    self.name = name
    self.roll_number = roll_number
    self.cgpa = cgpa


def sort_Students(students_list):
  # Sort the list if students in descending order of CGPA
  sorted_students = sorted(students_list,key=lambda student: student.cgpa, reverse=True)
  #Syntax - lambda arg:exp
  return sorted_students


# Example usage:
student =  [
  Students("Harl","A123",7.8),
  Students("Srikanth", "A124", 8.9),
  Students("Saumya", "A125", 9.1),
  Students("Mahidhar", "A126",9.9),
]

sorted_students = sort_Students(student)

# Print the sorted list of students
for student in sorted_students:
  print("Name: {}, Roll Number: {}, CGPA: {}".format(student.name,
                                                     student.roll_number, 
                                                     student.cgpa))