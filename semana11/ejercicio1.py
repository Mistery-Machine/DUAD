import math

class Circle: 
    def __init__(self, radius):
        self.radius = radius

    def calcule_circle(self):
        area=math.pi * self.radius *self.radius
        return area
    
radius = int(input("Enter the value of the radius of the circle you wanna calculate: "))
circle = Circle(radius)
area = circle.calcule_circle()

print(f"The area of the circle is {area}")