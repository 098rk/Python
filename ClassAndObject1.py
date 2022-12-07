# # 1)  The class called Holiday is started below.  An object of class Holiday represents a holiday
# # during the year.
# # This class has three instance variables:
# # ●	name, which is a String representing the name of the holiday
# # ●	day,which is an int representing the day of the month of the holiday
# # ● month, which is a String representing the month the holiday is in
# # a)Write a constructor for the class Holiday, which takes a String representing the name,
# # an int representing the day, and a String representing the month as its arguments, and sets the class variables to
# # these values.
# # b)	Write a method inSameMonth, which compares two instances of the class Holiday, and returns the
# # Boolean value  true if they have the same month, and false if they do not.
# # c)	Write a method avgDate which takes an
# # array of base type Holiday as its argument, and returns a double that  is the average of the day variables in the
# # Holiday instances in the array. You may assume that the array is full (i.e. does not have any null entries).
# # d) Write a piece of code that creates a Holiday instance with the name “Independence Day”, with the day “4”,
# # and with the month “July”.
# # =====================================================================================================
class Holiday:
    holiday_name = []
    holiday_month = []
    holiday_day = []

    def __init__(self, name, day, month):
        self.name = name
        self.day = day
        self.month = month
        Holiday.holiday_name.append(name)
        Holiday.holiday_month.append(month)
        Holiday.holiday_day.append(day)

    def get_month(self):
        return self.month

    def inSameMonth(self, obj_month):
        if self.month == obj_month:
            return True
        else:
            return False

    @staticmethod
    def avgDate():
        return sum(Holiday.holiday_day) / len(Holiday.holiday_day)


h = Holiday("Republic day", 26, "Jan")
h1 = Holiday("Maharashtra day", 1, "May")
# h1.append_name(h1.name)
# h1.append_month(h1.month)
# h1.append_day(h1.day)
# print(Holiday.holiday_name)
# print(Holiday.holiday_month)
# print(Holiday.holiday_day)
# Q1.b
print(h1.inSameMonth("May"))
# Q1.c
print(f"The avg of day for all holiday :{Holiday.avgDate()}")
# Q1.d
h2 = Holiday("Independence day", 4, "July")
# h2.append_name(h2.name)
# h2.append_month(h2.month)
# h2.append_day(h2.day)
print(f"Holiday names :{Holiday.holiday_name}")
print(f"Holiday Month :{Holiday.holiday_month}")
print(f"Holiday Day :{Holiday.holiday_day}")
