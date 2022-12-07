# 23 : Write a program to enter the numbers till the user wants and at the end the program should display the largest
# and smallest numbers entered

num=int(input("Enter the number till which you want want a list of number: "))
x=[]
for i in range(num):
    c=int(input("Enter the number you want to add in the list: "))
    x.append(c)
print(x)
print(f"The max value of the above enter range is {max(x)}")
print(f"The min value of the above enter range is {min(x)}")


