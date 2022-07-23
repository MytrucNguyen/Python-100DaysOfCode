# new_dict = {new_key: new_value for (key, value) in dict.items()}
import random

names = ["Alex", "Bob", "Cat", "Dave"]

student_scorees = {student: random.randint(1, 100) for student in names}
print(student_scorees)

passed_students = {student: score for (student, score) in student_scorees.items()  if score > 59 }
print(passed_students)