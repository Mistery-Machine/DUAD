class Device:  
  def __init__(self, brand, model, type):  
    self.brand = brand
    self.model = model
    self.type = type  

  def show_basic_info(self):  
    return f"The model is {self.model} and the brand is {self.brand}"

  
class Phone(Device):  
  def __init__(self, brand, model, number_of_cameras, type):  
    super().__init__(brand, model, type)  
    self.number_of_cameras = number_of_cameras
  
  def show_basic_info(self):
    return f"{super().show_basic_info()} and it has {self.number_of_cameras} cameras"

  
class Computer(Device):  
  def __init__(self, brand, model, type):  
    super().__init__(brand, model, type)  
  
  def show_basic_info(self):
    return f"{super().show_basic_info()} and the computer is a {self.type}"


class Smartphone(Phone, Computer):  
  def __init__(self, brand, model, number_of_cameras, type):  
    Phone.__init__(self, brand, model, number_of_cameras, type)  
  
  def show_basic_info(self):
    return f"{super().show_basic_info()} and it is a {self.type} device"


phone = Phone("Samsung", "Galaxy S23", 3, "smartphone")  
computer = Computer("Apple", "MacBook Pro", "laptop")
smartphone = Smartphone("Apple", "iPhone 15", 2, "hybrid")

print(phone.show_basic_info())
print(computer.show_basic_info())
print(smartphone.show_basic_info())