class PositiveNumber:
    def __init__(self, name):
        self.name = "_" + name

    def __get__(self, instance, owner):
        return getattr(instance, self.name)

    def __set__(self, instance, value):
        if value < 0:
            raise ValueError(f"{self.name[1:]} must be positive")
        setattr(instance, self.name, value)
