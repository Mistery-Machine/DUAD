from abc import ABC, abstractmethod
import math

class Shape (ABC): 
  @abstractmethod
  def calculate_perimeter(self): 
    pass

  @abstractmethod
  def calculate_area(self): 
    pass

class Circle(Shape): 
  def __init__(self, radius):
    self.radius = radius
  
  def calculate_perimeter(self):
    return 2*math.pi*self.radius
  
  def calculate_area(self):
    return math.pi*(self.radius**2)
  
class Rectangle(Shape): 
  def __init__(self, width, height):
    self.width = width
    self.height = height 

  def calculate_perimeter(self):
    return (2*self.width) + (2*self.height)
  
  def calculate_area(self):
    return self.width * self.height
  
class Triangle (Shape): 
  def __init__(self, side,base, height):
    self.side = side 
    self.base = base
    self.height = height 
  
  def calculate_perimeter(self):
    return 3*self.side
  
  def calculate_area(self):
    return (self.base * self.height)/2
  

my_circle = Circle(5)
my_triangle = Triangle(5,6,7)
my_rectangle = Rectangle(5,6)

print(f"The circle's perimeter is {my_circle.calculate_perimeter()} and the area is {my_circle.calculate_area()}")
print(f"The perimeter of the rectangle is {my_rectangle.calculate_perimeter()} and the area is {my_rectangle.calculate_area()}")
print(f"The perimeter of the triangle is {my_triangle.calculate_perimeter()} and the area is {my_triangle.calculate_area()}")