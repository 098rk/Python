# 24 : Write a program with a function that accepts a string from keyboard and create a new string after converting
# character of each word capitalized. For instance, if the sentence is "stop and smell the roses." the output should
# be "Stop And Smell The Roses".

s = 'stop and smell the roses'
# file = open('note.txt', 'r+')
# s = file.read()
# print(s)
x = s.split()
# print(x)
for i in x:
    y = i[0:1].upper()
    z = i[1:].lower()
    print(y + z, end=" ")






# ================
# s = 'stop and smell the roses'
# print(s)
# x = s.split()
# print(x)
# for i in range(0, len(x)):
#     # y = x[i][0].upper()
#     # j=x.insert()
#     y=x[i]
#     y.s
#     print(y)
#     # x.append(y)
# # print(x)
#
# # x=s.replace(s[0],s[0].upper())
# # print(x)
