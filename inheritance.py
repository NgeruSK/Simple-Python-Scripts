class Vehicle:
    def GeneralUse(self):
        self.generaluse = "Movement"
    

class MotorCycle(Vehicle):
    def __init__(self, id) -> None:
        self.wheels =  2
        self.has_roof = False
        self.id = id
        self.specific_use = "Riding"

class Car(Vehicle):
    def __init__(self, id) -> None:
        self.wheels =  4
        self.has_roof = True
        self.id = id
        self.specific_use = "Driving"

Ma3 = Car(4545)
Ma3.GeneralUse()
print("Car roof status:",Ma3.has_roof)

Bikey = MotorCycle(5690)
print("Motorbike roof status:", Bikey.has_roof)
    

