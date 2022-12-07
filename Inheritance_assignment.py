"""Exercise on Inheritance:
-------------------------
Create a base class named Employee as follows:
Employee (
-- class variables and methods
	organisation_name,
	get_organisation_name(),
	set_organisation_name(org_name)

-- instance variables and methods()
emp_id,
name,
base_location,
deployed_location,
designation,
salary ,
get_employee_details()

Create a subclass of Employee named Manager as follows:
Manager(
-- instance variables and methods()
	managed_employees[],
	perform_appraisal_for_an_employee(emp_id,percent_raise),
	get_manager_details(mgr_id)
)

Write a main method that does the following:
create 3 objects of Employee
create an object of Manager_class and add the above 3 employee objects created as managed employees
display get_manager_details()
for an employee do perform_appraisal_for_an_employee()
"""

#
# class Employee:
#     organization_name = 'CDAC'
#
#     @classmethod
#     def get_organization_name(cls):
#         return cls.organization_name
#
#     @classmethod
#     def set_organization_name(cls, rcv_org_name):
#         cls.organization_name = rcv_org_name
#
#     def __init__(self, emp_id, name, base_location, deployed_location, designation, salary):
#         self.emp_id = emp_id
#         self.name = name
#         self.base_location = base_location
#         self.deployed_location = deployed_location
#         self.designation = designation
#         self.__salary = salary
#
#     def get_employee_details(self):
#         return f"Employee Details :: Employee ID: {self.emp_id},Employee Name: {self.name},Base location: " \
#                f"{self.base_location},Deployed location: {self.deployed_location},Designation: {self.designation} "
#         # return self.emp_id + " " + self.name + " " + self.base_location + " " + self.deployed_location + " " + \
#         #        self.designation
#
#     def set_salary(self, per):
#         self.__salary = self.__salary + ((self.__salary * per) / 100)
#
#     def get_salary(self):
#         return self.__salary
#
#
# class Manager(Employee):
#     def __init__(self, emp_id, name, base_location, deployed_location, designation, salary, managed_emp):
#         super().__init__(emp_id, name, base_location, deployed_location, designation, salary)
#         self.managed_Employee = []
#         self.managed_Employee.extend(managed_emp)
#
#     def get_employees_list(self):
#         for m in self.managed_Employee:
#             print(m.get_salary())
#
#     def perform_appraisal_for_an_employee(self, empId, percent_raise):
#         for e in self.managed_Employee:
#             if e.emp_id == empId:
#                 e.set_salary(percent_raise)
#                 break
#
#
# emp1 = Employee(1, "Hrishi", "pune", "mumbai", "Developer", 500000)
# emp2 = Employee(2, "omkar", "mumbai", "pune", "SqlDev", 600000)
# emp3 = Employee(3, "xyz", "delhi", "noida", "DevOps", 700000)
#
# print(emp1.get_employee_details())
# print(emp2.get_employee_details())
# print(emp3.get_employee_details())
#
# lists = [emp1, emp2, emp3]
# m1 = Manager(101, "John", "Dubai", "NewYork", "CEO", 10000000, lists)
#
# m1.perform_appraisal_for_an_employee(2, 10)
# print(emp2.get_salary())
# print(m1.g)


# =================================================================================================

# ----------------------------------------------
# Solution to Day11.txt Exercises:
# ----------------------------------------------
# Create a base class named Employee :
class Employee:
    # class variables and methods
    organisation_name = "CDAC"

    @classmethod
    def get_organisation_name(cls):
        return cls.organisation_name

    @classmethod
    def set_organisation_name(cls, org_name):
        cls.organisation_name = org_name

    # instance variables
    def __init__(self, rcv_emp_id, rcv_name, rcv_base_location, rcv_deployed_location, rcv_designation, rcv_salary):
        self.emp_id = rcv_emp_id
        self.name = rcv_name
        self.base_location = rcv_base_location
        self.deployed_location = rcv_deployed_location
        self.designation = rcv_designation
        self.salary = rcv_salary

    # Overloaded function
    def get_employee_details(self, honorific_titles):
        print(
            f"\n-----------------------------------\n{self.designation} {honorific_titles} {self.name} Details are:\
        \nEmpid:{self.emp_id},Name:{honorific_titles}{self.name},Base Location:{self.base_location},Deployed Location : {self.deployed_location},Designation:{self.designation},Salary:{self.salary}")

    # instance methods()
    def get_employee_details(self):
        print(
            f"\n-----------------------------------\n{self.designation} {self.name} Details are:\
        \nEmpid:{self.emp_id},Name:{self.name},Base Location:{self.base_location},Deployed Location : {self.deployed_location},Designation:{self.designation},Salary:{self.salary}")


# sub class Manager that inherits from Base class Employee
class Manager(Employee):

    # instance variables
    def __init__(self, rcv_emp_id, rcv_name, rcv_base_location, rcv_deployed_location, rcv_designation, rcv_salary,
                 rcv_managed_employees):
        super().__init__(rcv_emp_id, rcv_name, rcv_base_location, rcv_deployed_location, rcv_designation, rcv_salary)
        self.managed_employees = rcv_managed_employees

    # instance methods()
    def perform_appraisal_for_an_employee(self, emp_obj, percent_raise):
        current_salary = emp_obj.salary
        increment = current_salary * percent_raise / 100
        emp_obj.salary = current_salary + int(increment)

    def get_manager_details(self):
        # self.get_employee_details() # because I overrided in Manager I had comment this
        super().get_employee_details()
        print("Managed employees:  ", end=" ")
        for val in self.managed_employees:
            print(f"{val.name}", end=",")

    # overloaded the  get_employee_details received from the base class
    def get_employee_details(self, honorific_titles):
        print(
            f"\n-----------------------------------\n{self.designation} {honorific_titles} {self.name} Details are:\
        \nEmpid:{self.emp_id},Name:{honorific_titles}{self.name},Base Location:{self.base_location},Deployed Location : {self.deployed_location},Designation:{self.designation},Salary:{self.salary}")


# main method
# create 3 objects of Employee
e1 = Employee(100, "Gaurav", "Pune", "Bangalore", "Developer", 100)
e2 = Employee(200, "Pratik", "Chennai", "Bangalore", "Senior Developer", 200)
e3 = Employee(300, "Hemant", "Delhi", "Bangalore", "Architect", 300)

# create an object of Manager_class and add the above 3 employee objects created as managed employees
m1 = Manager(400, "Elon Musk", "California", "Pune", "Manager", 1000, [e1, e2, e3])

# display get_manager_details()
m1.get_manager_details()

# for an employee do perform_appraisal_for_an_employee()
print("\n-----------------------------------\nBefore Appraisal ")
e1.get_employee_details()
m1.perform_appraisal_for_an_employee(e1, 100)
print("-----------------------------------\nAfter Appraisal ")
e1.get_employee_details()

m1.get_employee_details('Mr')
