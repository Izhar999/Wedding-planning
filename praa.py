class Vehicle:
    def __init__(self,name,max_speed,mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage
    def seat_capacity(self,capacity):
        return (f"the seating capacity of a{self.name} is {capacity}")

class Bus(Vehicle):
    def seat_capacity(self, capacity=50):
        return super().seat_capacity(capacity=50)

school_bus=Bus("School Volvo",180,10)
print(school_bus.seat_capacity())
 