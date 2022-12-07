# 10.create a class named "CDAC_course"
# class variable
# 	instructors_so_far_for_the_course[] // list
# instance variables
# 	subject_name (public)
# 	subject_instructor_name (public)
# 	subject_instructor_designation ( protected)
# 	subject_instructor_company ( protected)
# 	subject_instructor_feedback ( private)
#
# instance methods
#    get_subject_instructor_feedback()
#
# classmethod
#    get_instructors_so_far_for_the_course()
#    // append to the existing list in this func
#    set_instructors_so_far_for_the_course(instructor_name)
#
# create a function main that
# a) creates an obj of course class with values
#    DIOT-Python,Elon Musk,CEO at Tesla ,Cdac,"Sample Feedback"
# b) Add Elon musk to the class list variable instructors_so_far_for_the_course
# c) print Elon Musk feedback
# d) Print all the instructors_so_far_for_the_course
#
class CDAC_Course:
    instructors_so_far_for_the_course = []  # class Variable

    def __init__(self, subject_name, subject_instructor_name, subject_instructor_designation,
                 subject_instructor_company, subject_instructor_feedback):  # constructor with instance variable
        self.subject_name = subject_name
        self.subject_instructor_name = subject_instructor_name
        self._subject_instructor_designation = subject_instructor_designation
        self._subject_instructor_company = subject_instructor_company
        self.__subject_instructor_feedback = subject_instructor_feedback

    def get_subject_instructor_feedback(self):  # instance method
        return self.__subject_instructor_feedback

    @classmethod
    def get_instructors_so_far_for_the_course(cls):  # Getter
        return cls.instructors_so_far_for_the_course

    @classmethod
    def set_instructors_so_far_for_the_course(cls):  # Setter
        no = int(input("Enter no of the instructor to add: "))
        for i in range(0, no):
            name = input("Enter the name of instructor : ")
            cls.instructors_so_far_for_the_course.append(name)


c1 = CDAC_Course("DOIT-Python", "Elon Musk", "CEO at Tesla", "CDAC", "Sample Feedback")  # object created for class

c1.set_instructors_so_far_for_the_course()
print(c1.get_instructors_so_far_for_the_course())  # printing all class variable
# print(c1.get_instructors_so_far_for_the_course())  # printing class variable
print(c1.get_subject_instructor_feedback())  # printing the feedback of instructor

# ==================================Vaibhav_code=================

# class CDAC_course:
#     instructors_so_far_for_the_course = ["madhura", "gaurav", "Tukdeo"]
#
#     def __init__(self, subject_name, subject_instructor_name, subject_instructor_designation,
#                  subject_instructor_company,
#                  subject_instructor_feedback):
#         self.subject_name = subject_name
#         self.subject_instructor_name = subject_instructor_name
#         self.subject_instructor_designation = subject_instructor_designation
#         self.subject_instructor_company = subject_instructor_company
#         self.subject_instructor_feedback = subject_instructor_feedback
#
#     def get_subject_instructor_feedback(self):
#         return self.subject_instructor_feedback
#
#     @classmethod
#     def get_instructors_so_far_for_the_course(cls):
#         return cls.instructors_so_far_for_the_course
#
#     @classmethod
#     def set_instructors_so_far_for_the_course(cls):
#         no = int(input("No of Instructors to add "))
#         for i in range(0, no):
#             name = input("Enter the name ")
#             cls.instructors_so_far_for_the_course.append(name)
#
#
# c1 = CDAC_course("DIOT-Python", "Elon Musk", "CEO at Tesla", "Cdac", " Sample Feedback")
#
# print(c1.get_instructors_so_far_for_the_course())
# print(c1.get_subject_instructor_feedback())
# c1.set_instructors_so_far_for_the_course()
# print(c1.get_instructors_so_far_for_the_course())
