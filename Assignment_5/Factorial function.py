def factorial():
    num = int(input("Enter the number for which factorial to be calculated: "))
    fact = 1
    for i in range(1, num+1):
        fact = fact*i
    print(fact)


factorial()
