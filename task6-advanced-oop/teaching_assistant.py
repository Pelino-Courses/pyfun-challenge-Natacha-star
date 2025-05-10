from student import Student
from instructor import Instructor

class TeachingAssistant(Student, Instructor):
    def __init__(self, name: str, email: str):
        Student.__init__(self, name, email)
        Instructor.__init__(self, name, email)

    def get_role(self) -> str:
        return "TeachingAssistant"

    def __str__(self):
        return f"TeachingAssistant({self.name})"
