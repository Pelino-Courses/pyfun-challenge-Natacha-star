from typing import List, Iterator
from person import Person
from enrollment import Enrollment

class Student(Person):
    def __init__(self, name: str, email: str):
        super().__init__(name, email)
        self.enrollments: List[Enrollment] = []

    def enroll(self, course):
        from course import Course
        enrollment = Enrollment(self, course)
        self.enrollments.append(enrollment)
        course.enrolled_students.append(self)

    def __iter__(self) -> Iterator:
        return (enrollment.course for enrollment in self.enrollments)

    def get_role(self) -> str:
        return "Student"

    def __str__(self):
        return f"Student({self.name})"

    def __add__(self, other):
        if not isinstance(other, Student):
            raise TypeError("Can only combine with another Student")
        combined_courses = list(set(self.enrollments + other.enrollments))
        return combined_courses
