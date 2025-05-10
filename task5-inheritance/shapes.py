#answers for question 5
        import math

class Shape:
    """
    Base class for geometric shapes.

    Attributes:
        name (str): Name of the shape.
    """

    def __init__(self, name):
        self.name = name

    def area(self):
        """
        Calculate the area of the shape.
        Should be overridden by subclasses.
        """
        raise NotImplementedError("Subclasses must implement area method.")

    def __str__(self):
        return f"{self.name} Shape"


class Circle(Shape):
    """
    Circle shape.

    Attributes:
        radius (float): Radius of the circle.
    """

    def __init__(self, radius):
        if radius <= 0:
            raise ValueError("Radius must be positive.")
        super().__init__("Circle")
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

    def __str__(self):
        return f"{super().__str__()} with radius {self.radius}"


class Rectangle(Shape):
    """
    Rectangle shape.

    Attributes:
        width (float): Width of the rectangle.
        height (float): Height of the rectangle.
    """

    def __init__(self, width, height):
        if width <= 0 or height <= 0:
            raise ValueError("Width and height must be positive.")
        super().__init__("Rectangle")
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def __str__(self):
        return f"{super().__str__()} with width {self.width} and height {self.height}"


class Triangle(Shape):
    """
    Triangle shape.

    Attributes:
        base (float): Base of the triangle.
        height (float): Height of the triangle.
    """

    def __init__(self, base, height):
        if base <= 0 or height <= 0:
            raise ValueError("Base and height must be positive.")
        super().__init__("Triangle")
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height

    def __str__(self):
        return f"{super().__str__()} with base {self.base} and height {self.height}"

    @classmethod
    def from_sides(cls, side1, side2):
        """
        Alternative constructor to create a triangle where base and height are set to the two sides.
        """
        return cls(side1, side2)


if __name__ == "__main__":
    
    shapes = []

    # Circle
    r = float(input("Enter radius for circle: "))
    circle = Circle(r)
    shapes.append(circle)

    # Rectangle
    w = float(input("Enter width for rectangle: "))
    h = float(input("Enter height for rectangle: "))
    rectangle = Rectangle(w, h)
    shapes.append(rectangle)

    # Triangle
    b = float(input("Enter base for triangle: "))
    ht = float(input("Enter height for triangle: "))
    triangle = Triangle(b, ht)
    shapes.append(triangle)

    print("\nShape Information:")
    for shape in shapes:
        print(f"{shape} → Area: {shape.area():.2f}")







