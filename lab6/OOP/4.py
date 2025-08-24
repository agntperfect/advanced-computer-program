import math
class Shape:
    def area(self):
        print("Area method not implemented in base class")

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius * self.radius


shapes = [Rectangle(5, 3), Circle(4)] 
for s in shapes:
    print(f"{s.__class__.__name__} area = {s.area()}")