# 19. Write a function in Python to count uppercase character in a text file "notes.txt"
import re

#
#
# def letter_counter():
#     count = 0
#     pattern = '[A-Z]'
#     with (open('note.txt', "r")) as file1:
#         for i in file1:
#             x = i.split(" ")
#             print(x)
#             for word in x:
#                 find = re.findall(pattern, x)
#                 if find:
#                     count += 1
#         print(f"The count of uppercase letter in the string is {count}")
#
#
# letter_counter()

file = open('note.txt', 'r')
x = file.read()
print(x)
pattern = '[A-Z]'


def letter_counter(string1):
    for word in string1:
        count = len(re.findall(pattern, string1))
    print(f"The count of uppercase letter in the string is {count}")


letter_counter(x)
file.close()
