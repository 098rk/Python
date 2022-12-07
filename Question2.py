# 2: Write a Python program that accepts number of subjects and then a list of subject names and a list marks.
# Print subject name and marks in order of its first occurrence comma separated.
# Sample Input:Number of subjects: 3
# Input Subject name : Bengali & Input Subject marks : 23
# Input Subject name : English & Input Subject name : 24
# Input Subject name : Math & Input Subject name : 45
# Sample output : Bengali--23 , English--24, Math--45
subject = []
marks = []
Number_of_subject = int(input("Enter the number of subject : "))
for i in range(Number_of_subject):
    subject.append(input("Enter the Subject name: "))
for i in range(Number_of_subject):
    marks.append(input("Enter the marks for required subject: "))
# print(subject)
# print(marks)
# for i in subject:
#     for j in marks:
#         x = (i, j)
#     print(x)
for i in range(0, len(subject)):
    print(subject[i], "--", marks[i])

# Vaibhav code-
# subject = []
# marks = []
# number_of_subject = int(input("Number of subjects::"))
#
# for i in range(number_of_subject):
#     subject.append(input("Subject Name::"))
#
# for i in range(number_of_subject):
#     marks.append(input("Subject marks::"))
#
# new_dict = {subject[i]: marks[i] for i in range(len(subject))}
#
# print(new_dict)
