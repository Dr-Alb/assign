class Superhero:
    def __init__(self, name, power, origin):
        self.name = name
        self.power = power
        self.origin = origin

    def introduce(self):
        print(f"I am {self.name}, my power is {self.power}!")

    def use_power(self):
        print(f"{self.name} uses {self.power}!")

# Inherited class with additional attributes and methods
class TechHero(Superhero):
    def __init__(self, name, power, origin, gadget):
        super().__init__(name, power, origin)
        self.gadget = gadget

    def use_power(self):
        print(f"{self.name} activates their {self.gadget} to unleash {self.power}!")

hero1 = Superhero("Alb", "Water Blast", "Nakuru")
hero2 = TechHero("Timothy", "Laser Beam", "Nairobi", "Arm Cannon")

hero1.introduce()
hero1.use_power()

print("----")

hero2.introduce()
hero2.use_power()


activity2

class Vehicle:
    def move(self):
        print("The vehicle is moving...")


class Car(Vehicle):
    def move(self):
        print("Driving on the road")

class Plane(Vehicle):
    def move(self):
        print("Flying in the sky ")

class Boat(Vehicle):
    def move(self):
        print("Sailing on water ")

# Function to demonstrate polymorphism
def vehicle_action(vehicle):
    vehicle.move()

# Creating the needed objects
my_car = Car()
my_plane = Plane()
my_boat = Boat()

# Using polymorphism in parent class
vehicle_action(my_car)
vehicle_action(my_plane)
vehicle_action(my_boat)
