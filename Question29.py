# 29 : Write a function that accepts a dictionary as an argument. If the dictionary contains replicate values,
# return an empty dictionary, otherwise, return a new dictionary whose values are now the keys and whose keys are the
# values.

Mydict=dict()
num = int(input("Enter the number of entry req: "))
for i in range(num):
    key = input("Enter the Key of dict: ")
    values = input("Enter the values of dict: ")
    Mydict[key]=values
# Mydict = {'Hrishi': '88', 'Omkar': '89', 'Alisha': '87'}


def duplicate_checker():
    New_dict = {}
    x = len(set(Mydict.values()))
    y = len(Mydict.values())
    print(x)
    print(y)
    if x != y:
        return New_dict
    else:
        for i in Mydict:
            # key = Mydict.values()
            # values = Mydict.keys()
            New_dict[Mydict[i]] = i
        return New_dict


print(duplicate_checker())
