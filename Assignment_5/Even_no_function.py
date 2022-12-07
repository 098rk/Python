def Even_no_function():
    num = int(input("Enter the number till which even number to be calculated: "))
    for i in range(1, num + 1):
        if i % 2 == 0:
            print(i)


Even_no_function()
