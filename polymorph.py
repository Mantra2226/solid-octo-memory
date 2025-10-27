# Example of polymorphism in Python with vehicles

class Vehicle:
    def move(self):
        raise NotImplementedError("Subclasses must implement this method")

class Car(Vehicle):
    def move(self):
        print("Driving 🚗")

class Plane(Vehicle):
    def move(self):
        print("Flying ✈️")

class Boat(Vehicle):
    def move(self):
        print("Sailing 🚤")

# Create objects
car = Car()
plane = Plane()
boat = Boat()

# Loop through the vehicles and call the move() method
for vehicle in (car, plane, boat):
    vehicle.move()
