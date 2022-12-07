# 6. Write a Python program to count the occurrence of each element of a given list.
# Sample :
# Original List:
# ['Green', 'Red', 'Blue', 'Red', 'Orange', 'Black', 'Black', 'White', 'Orange']
# Count the occurrence of each element of the said list:
# Counter({'Red': 2, 'Orange': 2, 'Black': 2, 'Green': 1, 'Blue': 1, 'White': 1})
# Original List:
# [3, 5, 0, 3, 9, 5, 8, 0, 3, 8, 5, 8, 3, 5, 8, 1, 0, 2]
# Count the occurrence of each element of the said list:
# Counter({3: 4, 5: 4, 8: 4, 0: 3, 9: 1, 1: 1, 2: 1})

# from collections import Counter

# My_list = []
# My_list = ['Green', 'Red', 'Blue', 'Red', 'Orange', 'Black', 'Black', 'White', 'Orange']
# My_list = [3, 5, 0, 3, 9, 5, 8, 0, 3, 8, 5, 8, 3, 5, 8, 1, 0, 2]
# Number_of_items = int(input("Enter the number of elements you want to add in list: "))
# for i in range(Number_of_items):
#     item=input("Enter the items to be added: ")
#     My_list.append(item)
# print(My_list)

# print(Counter(My_list))
# =============================================================

My_list = []
MyDict = dict()
Number_of_items = int(input("Enter the number of element you want to add in list"))
for i in range(Number_of_items):
    items = input("Enter the items to be added: ")
    My_list.append(items)
print(My_list)
for i in range(Number_of_items):
    count = 1
    for j in range(Number_of_items):
        if i == j:
            continue
        else:
            if My_list[i] == My_list[j]:
                count += 1
    MyDict[My_list[i]] = count
for i in MyDict.keys():
    print(f"{i},{MyDict[i]}")
