class Circle():
    pi = 22/7

    def __init__(self, radius=1):
        self.radius = radius
        self.area = (radius**2)*self.pi

    def circumference(self):
        return self.radius * self.pi * 2


var = Circle(7)
print(var.pi)
print(var.radius)
print(var.area)
print(var.circumference())
hello = Circle(14)
print(hello)
