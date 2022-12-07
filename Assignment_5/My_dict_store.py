# 2) Create a program named "my_dict_store" which support following operations on
# dictionary named "capitals" which would have keys as their country and values as their capitals
# respectively from the user
# for ex: "India" : "New Delhi" ,"USA" : "Washington DC","Nepal": "Kathmandu","Ukraine" : "Kyiv"
# is provided by the user
#
# Operations supported by our program are : 1: Display number of elements in the capitals collection 2: Add an
# element to the capitals collection like --> Afghanistan: Kabul 3: Add multiple elements to the capitals collection
# like -->  Albania:Tirana,Algeria:Algiers,Andorra:Andorra la Vella 4: Remove an element from the collection
#
# Keep asking the user for the operation in this store until he chooses to exit from the program

# =====================================================================================================================
# 1: Display number of elements in the capitals collection
# 2: Add an element to the capitals collection like  --> Afghanistan: Kabul
# 3: Add multiple elements to the capitals collection like -->  Albania:Tirana,Algeria:Algiers,Andorra:Andorra la Vella
# 4: Remove an element from the collection
# 5: Exit
# ======================================================================================================================
capitals = {}


def add_Country():
    key = input("Enter the country name: ")
    if key in capitals:
        print("The country is already present")
    else:
        value = input("Enter the capital name of the country: ")
        capitals[key] = value
    print(capitals)


flag = True
while flag:
    num = int(input("Enter the number of countries to add to dict: "))
    for i in range(num):
        add_Country()
    break
flag = True
while flag:
    print(" 1: Display number of elements in the capitals collection\n"
          "2:Add an element to the capitals collection like  --> Afghanistan: Kabul\n"
          "3: Add multiple elements to the capitals collection like -->  Albania:Tirana,Algeria:Algiers,"
          "Andorra:Andorra la Vella\n "
          "4: Remove an element from the collection\n")
    num = int(input("Enter the req operation to perform: "))
    if num == 1:
        print(len(capitals))
    elif num == 2:
        add_Country()
    elif num == 3:
        flag = True
        while flag:
            num = int(input("Enter the number of countries to add to dict: "))
            for i in range(num):
                add_Country()
            break
    elif num == 4:
        c = capitals.popitem()
        print("item popped:", c)
        print(capitals)
    x = input("Do you want to continue (Y or N): ")
    if x.lower() == 'y':
        print("continued")
    else:
        flag = False
        print("Exited!!!")
        break
