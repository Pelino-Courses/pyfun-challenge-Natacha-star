from typing import List
from person import Person

class Instructor(Person):
    def __init__(self, name: str, email: str):
        super().__init__(name, email)
        self.courses_taught = []

    def get_role(self) -> str:
        return "Instructor"

    def __str__(self):
        return f"Instructor({self.name})"
