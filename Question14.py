# 14. Below we've provided a list of tuples, where each tuple contains details about an employee of a shop.
# Print how much each employee is due to be paid at the end of the week in a nice, readable format.
employees = [
    ("Rolf Smith", 35, 8.75),
    ("Anne Pun", 30, 12.50),
    ("Charlie Lee", 50, 15.50),
    ("Bob Smith", 20, 7.00)]

for i in range(len(employees)):
    print(f"Employee:{employees[i][0]} is due to be paid with {employees[i][1]*employees[i][2]}")
