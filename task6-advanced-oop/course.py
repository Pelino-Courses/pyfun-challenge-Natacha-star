from typing import Iterator, List
from descriptors import PositiveNumber

class Course:
    credits = PositiveNumber("credits")

    def __init__(self, code: str, name: str, credits: int):
        self.code = code
        self.name = name
        self.credits = credits
        self.enrolled_students = []

    def __iter__(self) -> Iterator:
        return iter(self.enrolled_students)

    def total_enrolled(self) -> int:
        return len(self.enrolled_students)

    def __str__(self):
        return f"Course({self.code}: {self.name}, {self.credits} credits)"

    @classmethod
    def create_lab_course(cls, code, name):
        return cls(code, name, credits=1)

    @classmethod
    def create_full_course(cls, code, name):
        return cls(code, name, credits=3)
