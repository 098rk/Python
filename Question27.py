# 27: Write a program that keeps student's name and his marks in a dictionary as key-value pairs. The program should
# store records of 10 students and display students name and marks of five students in decreasing order of marks
# obtained.
Mydict = dict()
# Mydict = {'Hrishi': '88', 'Rohit': '89', 'Abhi': '87', 'Raman': '86', 'Sejal': '85', 'Bushan': '90', 'Sourabh': '82'}
num = int(input("Enter the number of student you want to enter: "))
for i in range(num):
    Key = input("Enter the name of student: ")
    value = input("Enter the marks of student: ")
    Mydict[Key] = value
# print(Mydict)
values = Mydict.values()
# print(values)
values2 = list(values)
# print(values2)
x = sorted(values2, reverse=True)
print(x)
# print(x[0])
# name = {i for i in Mydict if Mydict[i] == x[i]}
# print(name)

print("Second Lowest marks : ", values2[0:4])
name = {i for i in Mydict if Mydict[i] == x[0:4]}
print("Name of the student with Second-lowest marks: ", name)
