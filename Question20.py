# 20. Create a text file named "matter.txt" contains some text, which needs to be displayed such that every next
# character is separated by a symbol "#". Write a function definition for hash_display() in Python that would display
# the entire content of the file matter.txt in the desired format.
# Example :
# If the file matter.txt has the following content stored in it :
# THE WORLD IS ROUND
# The function hash_display() should display the following content :
# T#H#E# #W#O#R#L#D# #I#S# #R#O#U#N#D#

# print(string.split(" "))
# x = tuple(string)
# print(x)
# y = list(x)
# print(y)
# for i in range(0,len(y)):
#     if i%2==0:
#         y.insert(i, "#")
# print(y)
def hash_display():
    for i in string:
        print(i, end='#')


hash_display()
file = open('matter.txt', 'r+')
string = file.read()
print(string)
