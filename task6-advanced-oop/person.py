from abc import ABC, abstractmethod

class Person(ABC):
    def __init__(self, name: str, email: str):
        self.name = name
        self.email = email

    @abstractmethod
    def get_role(self) -> str:
        pass
