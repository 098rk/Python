# 17. Write a function in Python to count the words "this" and "these" present in a text file "notes.txt".
# [Note that the words "this" and "these" are complete words]
def word_counter(string1, string2):
    count1 = 0
    count2 = 0
    with(open('note.txt', 'r')) as file1:
        for i in file1:
            x = i.split()
            print(x)
            for word in x:
                if string1.lower() == word.lower():
                    count1 += 1
            for word_n in x:
                if string2.lower() == word_n.lower():
                    count2 += 1
    print(f"The word '{string1}' occurrence is {count1} and '{string2}' occurrence is {count2}")
    file1.close()


word_counter(input("Enter the 1st word the find: "), input("Enter the 2st word the find: "))

# ==================================vaibahv code===========================================
# import re
#
# file1 = open('note.txt', 'r')
#
#
# def find_number_of_occurance(file):
#     string = file1.read()
#     find_this = re.findall('this', string.lower())
#     find_these = re.findall('these', string.lower())
#     print(f"The Number of Occurrence of 'this' {len(find_this)} and 'these' {len(find_these)}")
#
#
# find_number_of_occurance(file1)
# file1.close()
