# 28: Write a program that keeps name and birthday in a dictionary as key-value pairs. The program should display a
# menu that lets the user search a person’s birthday, add a new name and birthday, change an existing birthday,
# and delete an existing name and birthday.

Mydict = dict()


def person_add():
    num = int(input("Enter the number of person to add: "))
    for i in range(num):
        key = input("Enter the name of person: ")
        value = input("Enter the DOB of person: ")
        Mydict[key] = value
    print(Mydict)


def search_person():
    x = input("Enter the name of person to find: ")
    if x.lower() in Mydict:
        print(Mydict[x])


def change_DOB():
    x = input("Enter the name of person whose DOB is to be changed: ")
    if x.lower() in Mydict:
        day = int(input("Enter the DOB: "))
        Mydict[x] = day
        print(Mydict)


def delete_item():
    Mydict.popitem()
    print(Mydict)


flag = True
while flag:
    print("----------------------------------------------------\n"
          "-----------------BirthDay Display-------------------\n"
          "1)Add Person name and Date of Birth: \n"
          "2)Search respective Date of Birth: \n"
          "3)Add a new person in the list: \n"
          "4)Change the respective person Date of Birth: \n"
          "5)Delete the last person from the list: \n"
          "6)End of Application: ")
    choice = int(input("Enter the choice of operation: "))
    if choice == 1:
        person_add()
    elif choice == 2:
        search_person()
    elif choice == 3:
        person_add()
    elif choice == 4:
        change_DOB()
    elif choice == 5:
        delete_item()
    else:
        flag = False
        print("End of program")
