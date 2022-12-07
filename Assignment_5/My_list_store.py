# --------------------------------------------------------------------------------------------------------
# Assignment/Exercises
# Topics covered : Modules,Functions,Looping,Conditional constructs,Input,Output,LIST Collections :
# -------------------------------------------------------------------------------------------
# 1) Create a program named "my_list_store"
# which support following operations on list named "members" which is provided by the user
# for ex: ["Pratiksha","Kevin","Sachin","Yuvraj","Sania"] is provided by the user
#
# Operations supported by our program are :
#   1:  Display number of elements in the members list
#   2:  Add an element to the members collection like 'Sehwag'
#   3:  Add elements to the members collection like ['David','Bret','Sanju']
#   4:  Remove a member from the collection at a given subscript
#   5:  Remove the last member from the collection
#   6:  Display third, fourth and fifth element from the collection
#
# Keep asking the user for the operation in this store until he chooses to exit from the program

members = []
flag = True
while flag:
    x = input("Enter the name of members to add to the list: ")
    members.append(x)
    y = input("Do you want to add next member to the list (Y OR N) : ")
    if y.lower() == 'y':
        print("The element added!!")
    else:
        flag = False
    print(members)
newflag = True
while newflag:
    print("1:Display number of elements in the members list:\n"
          "2:  Add an element to the members collection like 'Sehwag'\n"
          "3: Add elements to the members collection like ['David','Bret','Sanju']\n"
          "4 : Remove a member from the collection at a given subscript\n"
          "5: Remove the last member from the collection\n"
          "6: Display third, fourth and fifth element from the collection")
    num = int(input("Enter the operation you want to perform: "))
    if num == 1:
        print(len(members))
    elif num == 2:
        new_member = input("Enter the new member: ")
        members.append(new_member)
        print(members)
    elif num == 3:
        new_list = []
        n = int(input("Enter the no of elements to be added: "))
        for i in range(n):
            x = input("Enter the new list element:")
            new_list.append(x)
            print(new_list)
        members.append(new_list)
        print(members)
    elif num == 4:
        n = int(input("Enter the index no of list from which element needs to be removed: "))
        members.pop(n)
        print(members)
    elif num == 5:
        members.pop()
        print(members)
    elif num == 6:
        print(members[3:6])
    x = input("Do you want to continue (Y or N):")
    if x.lower() == 'y':
        print("Continued!")
    else:
        flag = False
        print("Exited!!!")
        break