# 5.Write a Python program to count most and least common characters in a given string.
# Original string:
# hello world
# Most common character of the said string: l
# The Least common character of the said string: h
# ==================================================================================================
s = "hello world"
str_list = []
MyDict = dict()
# for i in s:
#     str_list.extend(i)
# print(str_list)
#
# for i in range(len(s)):
#     count = 1
#     for j in range(1, len(s)):
#         if i == j:
#             continue
#         else:
#             if str_list[i] == str_list[j]:
#                 count += 1
#     MyDict[str_list[i]] = count

# for i in MyDict:
#     if MyDict[i] == max(MyDict.values()):
#         lis.append(i)
# print(lis, max(MyDict.values()))
#
# # for i in MyDict:
# #     if MyDict[i] == min(MyDict.values()):
# #         lis.append(i)
# # print(lis, min(MyDict.values()))
# =====================================================
max_lis = []
min_lis = []
for i in s:
    MyDict[i] = MyDict.get(i, 0) + 1
print(MyDict)
for i in MyDict:
    if MyDict[i] == max(MyDict.values()):
        max_lis.append(i)
print("The Most common char in list is ", max_lis, "with count -", max(MyDict.values()))

for i in MyDict:
    if MyDict[i] == min(MyDict.values()):
        min_lis.append(i)
print("The least common char in list is ", min_lis, "with count -", min(MyDict.values()))
# ======================================================================
# for i in lis:
#     print(i,":",min(MyDict.values()),end = " ")

# for i in MyDict:
#     if MyDict[i] == min(MyDict.values()):
#         lis.append(i)
# print(lis, min(MyDict.values()))
# ==========================
# s = 'why this is the z kolaveri di'
# str_list = []
# for i in s:
#     str_list.extend(i)
# print(str_list)
# str_set_list = list(set(str_list))
# no_of_occ = []
# count = 1
# for i in str_set_list:
#     for j in str_list:
#         if i == j:
#             count += 1
#     no_of_occ.append(count)
#     count = 1
# dict_of_str = dict(zip(str_set_list, no_of_occ))
# print(dict_of_str)
# dict_max = max(dict_of_str.values())
# print(type(dict_max))
# max_str = [i for i in dict_of_str if dict_of_str[i] == dict_max]
# print("Most common character is ", max_str)
# dict_min = min(dict_of_str.values())
# print(type(dict_max))
# min_str = [i for i in dict_of_str if dict_of_str[i] == dict_min]
# print("Least most common character is ", min_str)
