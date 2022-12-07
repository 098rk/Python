# --------------------
# Exercise
# -------------------
# Lets implement my_calculator() solution in Solution_Day04.py in OOP concepts
# 1) Accept two numbers from the user and print
# a) addition
# b) first number squared 2
# c) first number raised to number second number

class MyOOPSCalculator:
    def __init__(self, rcv_first_num, rcv_second_num):
        self.first_num = rcv_first_num
        self.second_num = rcv_second_num

    def my_addition(self):
        return self.first_num + self.second_num

    def my_square(self):
        return self.first_num ** 2

    def my_exponenation(self):
        return self.first_num ** self.second_num

    @classmethod
    def my_calculator(cls):
        print("1.)Addition")
        print("2.)Square")
        print("3.)Exponentiation")
        choice = int(input("Please enter your choice from above:"))
        if choice == 1:
            my_cal_add_object = MyOOPSCalculator(int(input("Please enter the first number: ")),
                                                 int(input("Please enter the second number :")))
            print("The addition of the numbers is : ", my_cal_add_object.my_addition())
        elif choice == 2:
            my_cal_sqr_object = MyOOPSCalculator(int(input("Please enter the first number : ")),
                                                 int(input("Please enter the second number: ")))
            print("The square of first number :", my_cal_sqr_object.my_square())
        elif choice == 3:
            my_cal_exp_object = MyOOPSCalculator(int(input("Please enter the first number: ")),
                                                 int(input("Please enter the second number: ")))
            print("The exponentiation of first to second number is : ", my_cal_exp_object.my_exponenation())

    @staticmethod
    def iterative_calculation():
        while True:
            print("Lets start !!!!")
            MyOOPSCalculator.my_calculator()
            c = input("Do you want to continue (Y/N)").lower()
            if c == 'n':
                break


MyOOPSCalculator.iterative_calculation()
