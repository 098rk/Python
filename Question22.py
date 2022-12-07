# 22 : Two numbers are entered through the keyboard. Write a program to find the value of one number raised to the
# power of another
base = int(input("Enter the base number: "))
exponent = int(input("Enter the exponent number: "))


def Power_cal(b, e):
    result = pow(b, e)
    return result


print(Power_cal(base, exponent))
