# Define the Vehicle class (superclass)
class Vehicle:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def display_info(self):
        print(f"{self.year} {self.make} {self.model}")


# Define the Car class (subclass of Vehicle)
class Car(Vehicle):
    def __init__(self, make, model, year, doors):
        super().__init__(make, model, year)
        self.doors = doors

    def display_info(self):
        super().display_info()
        print(f"Doors: {self.doors}")


# Define the ElectricCar class (subclass of Vehicle)
class ElectricCar(Vehicle):
    def __init__(self, make, model, year, battery_size):
        super().__init__(make, model, year)
        self.battery_size = battery_size

    def display_info(self):
        super().display_info()
        print(f"Battery Size: {self.battery_size} kWh")


# Function demonstrating polymorphism
def display_vehicle_info(vehicle):
    vehicle.display_info()


# Creating instances of Car and ElectricCar
car1 = Car("Toyota", "Corolla", 2020, 4)
car2 = Car("Honda", "Accord", 2021, 4)
electric_car = ElectricCar("Tesla", "Model S", 2022, 100)

# Displaying information using polymorphism
print("Car 1 Information:")
display_vehicle_info(car1)
print("\nCar 2 Information:")
display_vehicle_info(car2)
print("\nElectric Car Information:")
display_vehicle_info(electric_car)
