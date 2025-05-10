class Enrollment:
    def __init__(self, student, course):
        self.student = student
        self.course = course

    def __str__(self):
        return f"{self.student.name} enrolled in {self.course.name}"
