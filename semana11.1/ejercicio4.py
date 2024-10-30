class Head: 
  def __init__(self):
    self.eyes =2
    self.ears=2
    self.mouth=1
    self.nose=1
    
class Torso: 
  def __init__(self):
    self.organs["heart","lungs","stomach"]
  
class Arm: 
  def __init__(self):
    self.hands=Hand()

class Hand: 
  def __init__(self):
    self.fingers=10
  
class Leg: 
    def __init__(self):
      self.feet=Feet()

class Feet:
  def __init__(self):
    self.finger_toes=10

class Human:
  def __init__(self):
    self.head=Head()
    self.torso=Torso()
    self.left_arm=Arm()
    self.right_arm=Arm()
    self.left_leg=Leg()
    self.right_leg=Leg()