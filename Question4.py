# 4. Write a Python program to find the item with maximum frequency in a given list.
# Sample :
# Original list:
# [2, 3, 8, 4, 7, 9, 8, 2, 6, 5, 1, 6, 1, 2, 3, 2, 4, 6, 9, 1, 2]
# Item with maximum frequency of the said list:
# (2, 5)
# ==ANSWER=====================================================
# from collections import Counter

# My_list = []
# # My_list = [2, 3, 8, 4, 7, 9, 8, 2, 6, 5, 1, 6, 1, 2, 3, 2, 4, 6, 9, 1, 2]
# n = int(input("Enter the number of items you want to add to list: "))
# for i in range(n):
#     x = int(input("Enter the items to add to list: "))
#     My_list.append(x)
# print(My_list)
# c = Counter(My_list)
# print(c.most_common(2))
# New_list = []
# My_list.sort()
# print(My_list)
# for i in range(0, len(My_list)):
#     x = (My_list.count(i))
#     New_list.append(x)
# print(New_list)
# print(max(New_list))

# # =======================================================Vaibhav code
# original_list = [2, 3, 8, 4, 7, 9, 8, 2, 6, 5, 1, 6, 1, 2, 3, 2, 4, 6, 9, 1, 2]
# freq_dict = dict()
#
# for i in range(len(original_list)):
#     count = 1
#     for j in range(1, len(original_list)):
#         if original_list[i] == original_list[j]:
#             count += 1
#     freq_dict[original_list[i]] = count
#
# max_freq = max(freq_dict.values())
# max_freq_tuple = (freq_dict[max_freq], max_freq)
# print("Item with maximum frequency of the said list::", max_freq_tuple)

# =============================================================================
# My_list = []
freq_dict = dict()
My_list = [2, 3, 8, 4, 7, 9, 8, 2, 6, 5, 1, 6, 1, 2, 3, 2, 4, 6, 9, 1, 2]
# n = int(input("Enter the number of items you want to add to list: "))
# for i in range(n):
#     x = int(input("Enter the items to add to list: "))
#     My_list.append(x)
# print(My_list)

for i in range(len(My_list)):
    count = 1
    for j in range(1, len(My_list)):
        if My_list[i] == My_list[j]:
            count += 1
    freq_dict[My_list[i]] = count

max_freq = max(freq_dict.values())
max_freq_tuple = (freq_dict[max_freq], max_freq)
print("Item with maximum freq of the list is : ", max_freq_tuple)
