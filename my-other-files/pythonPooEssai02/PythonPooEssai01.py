class Student:
    def __init__(self, name):
        self.name = name
        self.courses = []
        
    def enroll(self, course):
        self.courses.append(course)
        course.students.append(self)
        
class Course:
    def __init__(self, name):
        self.name = name
        self.students = []
        
    def add_student(self, student):
        self.students.append(student)
        student.courses.append(self)
        
class Enrollment:
    def __init__(self, student, course):
        self.student = student
        self.course = course


# Create some instances of the classes
s1 = Student("Alice")
s2 = Student("Bob")
c1 = Course("Math")
c2 = Course("English")

# Enroll students in courses
s1.enroll(c1)
s1.enroll(c2)
s2.enroll(c1)

# Add courses to students
c2.add_student(s2)