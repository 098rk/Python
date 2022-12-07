# 16.Write a function display_words() in python to read lines from a text file "notes.txt", and display those words,
# which are less than 4 characters.

def word_finder():
    # string = input("Enter the word you want the find in the file:")
    count = 0
    with (open('note.txt', "r")) as file1:
        for i in file1:
            x = i.split(" ")
            # print(x)
            for word in x:
                if len(word) < 4:
                    count += 1
                    print(word)
    print(count)

    file1.close()


word_finder()


# =========================================
# file1 = open('note.txt', 'r')
#
# string = file1.read()
#
#
# def display_words(rcv_str):
#     string1 = rcv_str.strip(".").split(" ")
#     for word in string1:
#         if len(word) < 4:
#             print(word)
#
#
# display_words(string)
# file1.close()