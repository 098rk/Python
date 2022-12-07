# 1. Write a Python program that accept a number of words and then those number of words and Print the number of
# distinct words and number of occurrences for each distinct word according to their appearance.
# Input number of words: 7
# Input the words:
# Red,Green,Blue,Black,White,Blue,Green
# Output:"Number of distinct words are 5"
# Red : 1,Green: 2,Blue : 2,Black : 1,White : 1
# ===========================================================
My_list = ["Red", "Green", "Blue", "Black", "White", "Blue", "Green"]
# My_list = []
MyDict = dict()
Number_of_items_to_add = int(input("Enter the number of items to add:"))
# for i in range(Number_of_items_to_add):
#     list_item = input("Enter the items to be added: ")
#     My_list.append(list_item)
print(My_list)
for i in range(Number_of_items_to_add):
    count = 1
    for j in range(1, Number_of_items_to_add):
        if i == j:
            continue
        else:
            if My_list[i] == My_list[j]:
                count += 1
    MyDict[My_list[i]] = count

for i in MyDict.keys():
    print(f"{i}:{MyDict[i]}")

# print(My_list[1])
# x = My_list.count()
# print(x)

# from collections import Counter
#
# Mylist = []
# for i in range(int(input("Enter the number of words you want tho add to list: "))):
#     Mylist.append(input("Enter the words you want to add: "))
#
# print(Counter(Mylist))

# Mylist = []
# MyDict = dict()
# number_of_words = int(input("Enter  the number of words you want to add : "))
# for i in range(number_of_words):
#     Mylist.append(input("Enter the words : "))
#
# for i in range(len(Mylist)):
#     count =1
#     for j in range(1, len(Mylist)):
#         if i == j:
#             continue
#         else:
#             if Mylist[i]==Mylist[j]:
#                 count +=1
#
#     MyDict[Mylist[i]]=count
#
# for i in MyDict.keys():
#     print(f"{i}:{MyDict[i]}")
