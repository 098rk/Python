# 3.Write a Python program to find the second-lowest total marks of any student(s)
# from the given names and marks of each student using lists and lambda function.
# Input number of students, names and grades of each student.
# Sample Input:Input number of students: 3
# Name: Avik Das
# Total marks: 89
# Name: ayan Roy
# Total marks: 75
# Name: Sayan Dutta
# Total marks: 93
# Sample Output:Names and Marks of all students:
# [['Avik Das ', 89.0], ['ayan Roy', 75.0], ['Sayan Dutta', 93.0]]
# Second lowest Marks: 89.0
# Names: Avik Das
# ============ANSWER===========================
# Name = []
# Marks = []
# Number_of_students = int(input("Enter the number of students: "))
# for i in range(Number_of_students):
#     x = input("Enter the Name of students: ")
#     Name.append(x)
# for i in range(Number_of_students):
#     x = int(input("Enter the Marks of students: "))
#     Marks.append(x)
# New_list = []
# for i in range(len(Name)):
#     x = [Name[i], Marks[i]]
#     print(x)
#     New_list.append(x)
# print(New_list)
# Marks.sort()
# print("Second Lowest marks : ", Marks[1])
# print("Name of the student with Second-lowest marks: ", Name[Marks.index(Marks[1])])
# =============================================================================
# New_dict = dict()
# Number_of_student = int(input("Enter the number of students: "))
# for i in range(0, Number_of_student):
#     key = input("Enter the name of student: ")
#     value = int(input("Enter the marks of student: "))
#     New_dict[key] = value
# values = New_dict.values()
# Values2 = list(values)
# Values2.sort()
# print(Values2)
# print("The second lowest marks are :", Values2[1])
# name = {i for i in New_dict if New_dict[i] == Values2[i]}
# print(name)

# ===============================================================================
New_dict = dict()
Number_of_students = int(input("Enter the number of students: "))
for i in range(0, Number_of_students):
    key = input("Enter the Name of students: ")
    value = int(input("Enter the Marks of students: "))
    New_dict[key] = value
values = New_dict.values()
values2 = list(values)
values2.sort()
print(values2)
# print("Second Lowest marks : ", values2[1])
# name = {i for i in New_dict if New_dict[i]==values2[1]}
# print("Name of the student with Second-lowest marks: ", name)
