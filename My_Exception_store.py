# ------------------------------------------------
# Exercise : Exceptions
# -------------------------------------------------
# Create the following program named "my_exception_store" with the menu below :
#
# Welcome User , What would you like to do today ?
#     1) Create a positive numbered list
#     Note : raise an exception if the users inserts a negative number OR user creates an empty list
class negative_number_error(Exception):
    pass


class empty_list_error(Exception):
    pass


def create_positive_number_list(my_list):
    for i in range(0, int(input("Please enter number of elements to the positive list: "))):
        if (num := int(input("Enter the number to be added: "))) < 0:
            raise negative_number_error
        else:
            my_list.append(num)
    if len(my_list) == 0:
        raise empty_list_error
    print(my_list)


# 2) Create a negative  numbered list
# Note : raise an exception if the users inserts a positive number/Zero OR user creates an empty list


class positive_number_error(Exception):
    pass


class empty_list_error(Exception):
    pass


def create_negative_list(my_list):
    for i in range(int(input("Enter the number of elements you want to add: "))):
        if (num := int(input("Enter the element: "))) >= 0:
            raise positive_number_error
        else:
            my_list.append(num)
    if len(my_list) == 0:
        raise empty_list_error
    print(my_list)


# 3) Create a heterogeneous list
# Note : raise an exception if the users creates a homogenous list (all elements of same datatype)

class homogenous_list_error(Exception):
    pass


class empty_list_error(Exception):
    pass


def create_heterogeneous_list(my_list):
    for i in range(0, int(input("Please enter number of elements to the heterogeneous list: "))):
        datatype_choice = int(input("Please choose a datatype of the element to be added:\n "
                                    "1)int\n 2)float\n 3)str\n 4)tuple\n 5)list\n 6)set\n 7)dictionary"))
        if datatype_choice == 1:
            my_list.append(int(input("Please enter an integer to be added: ")))
        if datatype_choice == 2:
            my_list.append(float(input("Please enter an float to be added: ")))
        if datatype_choice == 3:
            my_list.append(input("Please enter a string to be added"))
        if datatype_choice == 4:
            my_list.append(tuple(input("Please enter a tuple to be added").split(",")))
        if datatype_choice == 5:
            my_list.append(input("Please enter a list to be added").split(","))
        if datatype_choice == 6:
            my_list.append(set(input("Please enter a set to be added").split(",")))
        if datatype_choice == 7:
            my_temp_tuple_list = []
            for str_elem in input("Please enter a dictionary to be added like key1:value1,key2:value2").split(","):
                my_temp_tuple_list.append(tuple(str_elem.split(":")))
            my_list.append(dict(my_temp_tuple_list))

    if len(my_list) == 0:
        raise empty_list_error

    print(my_list)

    is_heterogeneous = False
    for x in range(1, len(my_list)):
        if type(my_list[0] != type(my_list[x])):
            is_heterogeneous = True
            break

    if not is_heterogeneous:
        raise homogenous_list_error
    else:
        print("We received a Heterogeneous list")


def find_an_element(my_list):
    datatype_choice = int(input(
        '''Please choose a datatype of the element to be searched \n1)Int \n2)Float \n3)Str \n4)Tuple \n5)list 
        \n6)set \n7)Dictionary \n'''))
    print(datatype_choice)
    if datatype_choice == 1:
        input_val = int(input("Please enter an integer"))
    if datatype_choice == 2:
        input_val = float(input("Please enter a float"))
    if datatype_choice == 3:
        input_val = input("Please enter a string")
    if datatype_choice == 4:
        input_val = tuple(input("Please enter a tuple").split(","))
    if datatype_choice == 5:
        input_val = input("Please enter a list").split(",")
    if datatype_choice == 6:
        input_val = set(input("Please enter a set").split(","))
    if datatype_choice == 7:
        my_temp_tuple_list = []
        for str_elem in input("please enter a dict like key1:value1, key2:value2").split(","):
            my_temp_tuple_list.append(tuple(str_elem.split(":")))
            input_val = dict(my_temp_tuple_list)

    print(f"{input_val} found in provided list {my_list}:{input_val in my_list}")


def my_exception_store():
    my_positive_list = []
    my_negative_list = []
    my_het_list = []

    while True:
        try:
            print("1) Create a positive numbered list")
            print("2) Create a negative numbered list")
            print("3) Create a heterogeneous list")
            print("4) Check if the element is present in the list")
            print("5) Refresh the program to start with blank lists")
            print("6) Exit")

            choice = int(input("Please enter your choice!!! : "))
            if choice == 1:
                create_positive_number_list(my_positive_list)
            elif choice == 2:
                create_negative_list(my_negative_list)
            elif choice == 3:
                create_heterogeneous_list(my_het_list)
            elif choice == 4:
                print("Lists created are as below")
                print(f"1:{my_positive_list}")
                print(f"2:{my_negative_list}")
                print(f"3:{my_het_list}")

                while True:
                    check = int(input("Which of the below list you want to search from"))
                    if check == 1:
                        find_an_element(my_positive_list)
                        break
                    elif check == 2:
                        find_an_element(my_negative_list)
                        break
                    elif check == 3:
                        find_an_element(my_het_list)
                        break
                    else:
                        print("Please choose something from above")
            elif choice == 5:
                my_positive_list.clear()
                my_negative_list.clear()
                my_het_list.clear()
                print("Store restarted !!!!")
            elif choice == 6:
                break
            else:
                print("Please choose something from the above")
        except negative_number_error:
            print("We received a negative number in the list and I handled negative_number_error exception")
            my_positive_list.clear()
        except positive_number_error:
            print("We received a positive number in the list and I handled positive_number_error exception")
            my_negative_list.clear()
        except homogenous_list_error:
            print("We received a Homogenous list and I handled homogenous_list_error exception")
            my_het_list.clear()


my_exception_store()

