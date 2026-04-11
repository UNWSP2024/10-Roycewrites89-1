#Royce Daniel 4/10/2026 "car go"
class car:
    def __init__(self,make,year_model, speed):
        self.make = make
        self.model = year_model
        self.speed = speed
    def accelerate(self):
        self.speed = self.speed + 5

    def decelerate(self):
        self.speed = self.speed - 5

    def getspeed(self):
        return self.speed

mycar = car("Chrysler", 2005, 0)
print("Accelerating:")


for i in range(5):
    mycar.accelerate()
    print("Current speed:", mycar.getspeed())

print("\nBraking:")
for i in range(5):
        mycar.decelerate()
        print("Current speed:", mycar.getspeed())
