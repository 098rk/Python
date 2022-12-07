# 3)  Create a program named "my_set_store" which support following operations on two sets
#     provided by user
#
# for ex:
# 	A = {1,2,3,4,5}
# 	B = {18,19,20,21}
# is provided by the user
#
# Operations supported by our program are :
# 	1: Union
# 	2: Intersection
# 	3: A-B
# 	4: B-A
# 	5: Take an element from user and Display if that element is a member of set B
# 	6: Display number of elements in the set A
#   7: Display number of elements in the set B
# 	8: Add an element taken from the user to the set A
# 	9: Add multiple elements taken from the user to the set A
# 	10: Remove an element taken from the user from set A

A = {1, 2, 3, 4, 5}
B = {18, 19, 20, 21}
flag = True
while flag:
    num = int(input("Enter the req operation to be performed: "))
    if num == 1:
        union_set = A.union(B)
        print(union_set)
    elif num == 2:
        Intersection_set = A.intersection(B)
        print(Intersection_set)
    elif num == 3:
        Difference_set = A.difference(B)
        print(Difference_set)
    elif num == 4:
        Difference_set = B.difference(A)
        print(Difference_set)
    elif num == 5:
        x = int(input("Enter the element : "))
        print(x in B)
    elif num == 6:
        print(len(A))
    elif num == 7:
        print(len(B))
    elif num == 8:
        x = int(input("Enter the element : "))
        A.add(x)
        print(A)
    elif num == 9:
        num = int(input("Enter the req no of element be added: "))
        for i in range(num):
            n = int(input("Enter the element to be added: "))
            A.add(n)
            print(A)
    elif num == 10:
        num = int(input("Enter the req no of element be removed: "))
        A.remove(num)
        print(A)
    c = input("Do you want to continue (Y or N): ")
    if c.lower() == 'y':
        print("continue")
    else:
        flag = False
        print("Exited!!!")
        break
