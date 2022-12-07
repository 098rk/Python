# 21. Write a function character_A_M_Count() in Python, which should read each character of a text file STORY.TXT.
# It should count and display the occurrence of alphabets A and M (including small cases a and m too).
# Create a text file STORY.TXT with the below contents:
# Updated information
# As simplified by official websites.
# The character_A_M_Count() function should display the output as:
# A or a:4
# M or m :2

def character_A_M_Count(string):
    count_a = 0
    count_m = 0
    for i in string:
        if i.lower() == 'a':
            count_a += 1
        if i.lower() == 'm':
            count_m += 1
    return f"The count of A or a in string is {count_a} \n" \
           f"The count of M or m in string is {count_m}"


file1 = open('story.txt', 'r')
str = file1.read()
print(str)
print(character_A_M_Count(str))
