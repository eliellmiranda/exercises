# This program reads two student grades, calculates their average, and displays the result.
print('WELCOME TO THE GRADE AVERAGE CALCULATOR\nYou need to enter two grades for the student.')

grade1 = float(input('Enter the first grade: '))
grade2 = float(input('Enter the second grade: '))

average = (grade1 + grade2) / 2

print('The student’s average grade is: {}'.format(average))
