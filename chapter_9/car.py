class Car():
    """simple try to present car."""

    def __init__(self, make, model, year):
        """initialisation of attributes describing the car."""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """return of an elegantly formatted car description."""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

    def read_odometer(self):
        """displays mileage information"""
        print(f"This car has travelled {self.odometer_reading} km.")

    def update_odometer(self, mileage):
        """assign the specified value to the odometer of the vehicle. the change will be rejected
        if an attempt is made to roll back the odometer"""
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can not roll back the odometer of car!")

    def increment_odometer(self, kilometers):
        """incrementation of the odometer value by the specified value"""
        self.odometer_reading += kilometers


my_new_car = Car('audi', 'a4', 2019)
print(my_new_car.get_descriptive_name())

my_new_car.odometer_reading =23
my_new_car.read_odometer()