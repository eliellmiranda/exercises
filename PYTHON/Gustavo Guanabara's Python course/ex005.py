# Write a program that reads an integer and displays its predecessor and successor.

print("WELCOME! \nThis program shows the predecessor and successor of a number!")

num = int(input("Enter a number: "))

prev_num = num - 1
next_num = num + 1

print("The predecessor of the entered number is: {}\nand its successor is: {}".format(prev_num, next_num))
