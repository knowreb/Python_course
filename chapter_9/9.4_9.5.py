# 9.4 Number of persons served
class Restaurant():
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name.title()
        self.cuisine_type = cuisine_type.title()
        self.number_served = 0

    def describe_restaurant(self):
        print(f"My restaurant is {self.restaurant_name} and type of food is {self.cuisine_type}")

    def open_restaurant(self):
        print(f"{self.restaurant_name} is open at 12AM")

    def set_number_served(self, number_served):
        self.number_served = number_served

    def increment_number_served(self, add_served):
        self.number_served += add_served

restaurant = Restaurant('Splecione', 'Polish' )
restaurant.describe_restaurant()
restaurant.open_restaurant()

print(restaurant.restaurant_name)
print(restaurant.cuisine_type)


restaurant.set_number_served(215)
print(f"\nNumber served: {restaurant.number_served}")

restaurant.increment_number_served(30)
print(f"Number served: {restaurant.number_served}")

# 9.5 Login attempts
