class Person:
  def __init__(self,name ): 
    self.name = name 

class Bus: 
    def __init__(self, max_passengers):
        self.max_passenger = max_passengers  
        self.passengers = [] 

    def add_passenger(self, person):
        if len(self.passengers) < self.max_passenger: 
            self.passengers.append(person)
            print(f"{person.name} has entered the bus")
        else: 
            print("Bus is full")
    
    def remove_passenger(self, person_name):
       for passenger in self.passengers: 
          if passenger.name == person_name: 
             self.passengers.remove(passenger) 
             print(f"{person_name} has leave the bus")
             return
          print(f"{person_name} is not on the bus")

    def show_passengers(self): 
        if not self.passengers:
            return 0
        else: 
         print("Passengers on the bus")
        for passenger in self.passengers: 
             print(f"- {passenger.name}")    
        return len(self.passengers)


def menu (): 
   while True: 
    try:
        max_passengers = int(input("Enter the number of maximum passengers on the bus: "))
        if max_passengers <=0:
           print("The maximum number of passengers must be greater than 0")
           continue
        bus = Bus(max_passengers)
        break
    except ValueError:
      print("Enter only valid numbers")

   while True: 
        print("\n--- Menú ---")
        print("1. Add passenger")
        print("2. Leave passenger")
        print("3. Show passengers on bus")
        print("4. Log out")
        try:
            option = int(input("Select an option: "))
        except ValueError: 
           print("Error: Pls enter a valid option for the menu")

        if option == 1: 
           name =input("Enter the name of the passenger that wants to get in the bus: ")
           passenger = Person(name)
           bus.add_passenger(passenger)

        elif option ==2: 
            if bus.show_passengers() == 0:
              print (" There's no passengers on the bus yet ")
              continue
            name =input("Enter the name of the passenger that wants to get out of the bus: ")
            bus.remove_passenger(name)

              
        
        elif option ==3:
           bus.show_passengers()

        elif option ==4: 
           print("Loggin out")
           break

menu ()