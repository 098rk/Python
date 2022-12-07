# 9. Print a greeting to the screen, welcoming our user to the Tip Calculator.
# Ask the user how much the total bill is and store the value in a variable.
# Ask the user how much percent tip they want to give the waiter and store the value in a variable.
# Ask the user how many people they want to split the bill between and store the value in a variable.
# Calculate how much each of your friends has to pay if the bill, including tip, is equally spread among them.
# Round the result to two positions after the comma and print it to the console
# Sample1:
# When you input the following amounts:
# Total bill: 150
# Tip percentage: 12
# Split between people: 5
# The total amount paid by each person should be 33.60, not 33.6
#
# If the bill is 150 split between 5 people with a 12% tip,
# you can use this formula to calculate the final amount each person has to pay
# (feel free to use any other formula to get to the result!):  150/5 * 1.12
# Sample2 :
# If you enter the following values:
# Total bill: 180
# Tip percentage: 15
# Split between people: 4
# Output:
# Each person has to pay : 51.75
print("-----------------------------------------------------------------------------------")
print("-----------------------Welcome to the Tip Calculator-------------------------------")
print("-----------------------------------------------------------------------------------")
total_bill = float(input("Enter the total bill amount :: "))
percent_tip = float(input("Enter the percentage of tip for Waiter :: "))
bill_split = int(input("Enter the qty of person in which the bill is going to split :: "))

Split_amount = (total_bill + ((percent_tip / 100) * total_bill)) / bill_split
print("Each person has to pay :", format(Split_amount, ".2f"))
