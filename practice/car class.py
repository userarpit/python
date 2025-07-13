class Car:
    def __init__(self,color,mileage) -> None:
        self.color = color
        self.mileage = mileage

    def __str__(self) -> str:
        return f"The {self.color} car has {self.mileage:,.2f} miles"
    
blue_car = Car('Blue',20000)
red_car  = Car('Red',30000)

print(blue_car)
print(red_car)