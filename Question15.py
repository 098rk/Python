# 15. Write a function in Python to read lines from a text file "notes.txt". Your function should find and display
# the occurrence of the word "the".
# Note :
# Create a file "notes.txt" with the following content below:
# "India is the fastest-growing economy. India is looking for more investments around the globe. The whole world is
# looking at India as a great market. Most of the Indians can foresee the heights that India is capable of reaching."
# The output should be 5
#
def word_finder(string):
    # string = input("Enter the word you want the find in the file:")
    count = 0
    with (open('note.txt', "r")) as file1:
        for i in file1:
            x = i.split(" ")
            # print(x)
            for word in x:
                if string.lower() == word.lower():
                    count += 1
    return count
    file1.close()

print(word_finder(input("Enter the word you want the find in the file:  ")))

# ===============================geeksforgeeks=============
# Program to get letter count in a text file

# explicit function to return the letter count
# def letterFrequency(filename, letter):
#     # open file in read mode
#     file = open(filename.lower(), 'r')
#     # store content of the file in a variable
#     text = file.read()
#     x = text.lower()
#     print(x)
#     # using count()
#     return x.count(letter)
#
#
# # call the function and display the letter count
# print(letterFrequency('note.txt', 'the'))
