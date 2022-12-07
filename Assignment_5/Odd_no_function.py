def Odd_no_function():
    num = int(input("Enter the number till which odd number to be calculated: "))
    this_list = []
    for i in range(1, num + 1):
        if i % 2 != 0:
            print(i)
            this_list.append(i)
    this_tuple = tuple(this_list)
    print(this_tuple)


Odd_no_function()
