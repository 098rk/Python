# 7.Write a program that calculates a user's BMI using the user's weight and height.
# BMI is calculated by dividing the person's weight in kg by the square of the person's height in meters.
# Round the result to a whole number.
# Sample :
# height = 1.85
# weight = 75
# Output: 22

Height = float(input("Enter the height in meter format: "))
Weight = float(input("Enter the Weight in KG format : "))
BMI = (Weight / (Height ** 2))
print("The Body_Mass_Index(BMI) of the person is : ", round(BMI))
