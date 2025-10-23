""" The same teacher wants to randomly choose the order of 
students' presentations. Write a program that reads the names 
of four students and displays the randomized order.
"""
import random

student1 = input("Enter the name of the first student: ")
student2 = input("Enter the name of the next student: ")
student3 = input("Enter the name of the next student: ")
student4 = input("Enter the name of the next student: ")

names = [student1, student2, student3, student4]

random.shuffle(names)

print("The presentation order will be:")

for index, name in enumerate(names, start=1):
    print(f"{index} - {name}")