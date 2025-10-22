""" A teacher wants to randomly choose one of their
four students to clean the board. Create a program
to help with this task by reading the students’ names
and displaying the selected one.
"""


import random

student1 = input("Enter the name of student 1: ")
student2 = input("Enter the name of student 2: ")
student3 = input("Enter the name of student 3: ")
student4 = input("Enter the name of student 4: ")

students = [student1, student2, student3, student4]

chosen = random(students)

print(f"The chosen student is: {chosen} ")