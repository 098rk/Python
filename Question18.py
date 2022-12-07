# 18. Write a function in Python to count words in a text file "notes.txt" those are ending with alphabet "e"
import re


def word_counter():
    count = 0
    pattern = 'e$'
    with (open('note.txt', "r")) as file1:
        for i in file1:
            x = i.split(" ")
            print(x)
            for word in x:
                find = re.search(pattern, word)
                if find:
                    count += 1
        print(f"The count of word with ending letter 'e' is {count}")


word_counter()

# import re

# file1 = open('note.txt', 'r')
# string = file1.read()

#
# def find_number_of_occurance(rcv_str):
#     count = 0
#     pattern = 'e$'
#     string1 = rcv_str.strip(".").split(" ")
#     for word in string1:
#         find = re.search(pattern, word)
#         if find:
#             count += 1
#     print(f"The count of words ending with alphabet 'e':: {count}")
#
#
# find_number_of_occurance(string)
# file1.close()
#
# # f = open('note.txt', 'r')
# # x = f.read()
# w = "hello there is me hrishi"
# # search_op = re.search("e$", w)
# # count = 0
# # if search_op:
# #     count += 1
# # else:
# #     print("no word")
# # print(count)
# re.findall(r'e$', w)
