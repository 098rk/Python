# Exercise 01 : Classes and objects -- try creating this in oops world
# -------------------------------------------
# EmployeeExercise 01 : Classes and objects -- try creating this in oops world
# -------------------------------------------
# Employee
# # instance variables
# emp_id (Public)
# emp_salary (Private)
# mgr_id ( Public)
#
#
# # class variable
# department_name
#
# # instance methods
# get_emp_salary()-> emp_salary
# set_emp_salary(rcv_salary)-> emp_salary
#
#
# # class method
# get_department_name() --> department_name
#
# # static method
# field_expertise() --> just displays some values of expertise which is applicable
# for all my employees collectively
#
# main
#
#
# 1) create an object employee(100,1000,1)
# 2) do the following for the created object
# // direct access using .notation
# empire
# emp_salary
# mgr_id
# 3) print the department name
# 4) display the expertise for the employees
# 5) Deleting Attributes and Objects
#
# # instance variables
# emp_id (Public)
# emp_salary (Private)
# mgr_id ( Public)
#
#
# # class variable
# department_name
#
# # instance methods
# get_emp_salary()-> emp_salary
# set_emp_salary(rcv_salary)-> emp_salary
#
#
# # class method
# get_department_name() --> department_name
#
# # static method
# field_expertise() --> just displays some values of expertise which is applicable
# for all my employees collectively
#
# main
#
#
# 1) create an object employee(100,1000,1)
# 2) do the following for the created object
# // direct access using .notation
# empid
# emp_salary
# mgr_id
# 3) print the department name
# 4) display the expertise for the employees
# 5) Deleting Attributes and Objects

class Employee:
    department_name = 'Sales'

    def __init__(self, emp_id, emp_salary, mgr_id):
        self.emp_id = emp_id
        self.__emp_salary = emp_salary
        self.mgr_id = mgr_id

    def get_emp_salary(self):
        return self.__emp_salary

    def set_emp_salary(self, rcv_salary):
        self.__emp_salary = rcv_salary

    @classmethod
    def get_department_name(cls):
        return cls.department_name

    @staticmethod
    def field_expertise():
        print("Finance")


Employee1 = Employee(100, 1000, 1)

print(Employee1.emp_id)
print(Employee1.get_emp_salary())
print(Employee1.mgr_id)

print(Employee1.get_department_name())

Employee1.field_expertise()

del Employee1.emp_id
print(Employee1)
del Employee1.get_emp_salary
print(Employee1.get_emp_salary)
del Employee1.mgr_id
print(Employee1.mgr_id)

del Employee1
# print(Employee1)
