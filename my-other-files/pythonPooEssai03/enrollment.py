from student import Student
from course import Course

class Enrollment:
    def __init__(self, student, course):
        self.student = student
        self.course = course
        self.student.courses.append(course)
        self.course.students.append(student)