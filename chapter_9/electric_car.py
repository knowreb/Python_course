class Car():
    """Simple try to present the car"""
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

    def read_odometer(self):
        print(f"This car has travelled {self.odometer_reading} km.")

    def update_odometer(self, mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can not roll back the odometer of car!")

    def increment_odometer(self, kilometers):
        self.odometer_reading += kilometers

class ElectricCar(Car):
    """Present the characteristic of an electric car"""
    def __init__(self, make, model, year):
        """Initialisation of parent class attributes"""
        super().__init__(make, model, year)
        self.batery_size = 75

    def describe_battery(self):
        """Present an information about size of battery """
        print(f"This car has a bettery capacity of {self.batery_size} kWh.")

my_tesla = ElectricCar('tesla', 'model s', 2019)
print(my_tesla.get_descriptive_name())
my_tesla.describe_battery()
