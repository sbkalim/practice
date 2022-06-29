class Vehicle:
    def general_usage(self):
        print("General Use: Transportation")

class Cars(Vehicle):
    def __init__(self):
        print("I am car")
        self.wheels=4
        self.roof=True
    def specific_usage(self):
        print("Specific Use: Commute to Work, Family Vacation")

class Bikes(Vehicle):
    def __init__(self):
        print("I am Bike")
        self.wheels=2
        self.roof=False
    def specific_usage(self):
        print("Specific Use: Road Trip, Racing")

c=Cars()
c.general_usage()
c.specific_usage()

b=Bikes()
b.general_usage()
b.specific_usage()