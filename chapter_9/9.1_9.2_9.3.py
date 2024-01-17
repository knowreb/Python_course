# 9.1
class Restaurant():
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name.title()
        self.cuisine_type = cuisine_type.title()

    def describe_restaurant(self):
        print(f"My restaurant is {self.restaurant_name} and type of food is {self.cuisine_type}")

    def open_restaurant(self):
        print(f"{self.restaurant_name} is open at 12AM")

restaurant = Restaurant('Splecione', 'Polish' )
print(restaurant.restaurant_name)
print(restaurant.cuisine_type)
restaurant.describe_restaurant()
restaurant.open_restaurant()

# 9.2
class Restaurant():
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name.title()
        self.cuisine_type = cuisine_type.title()

    def describe_restaurant(self):
        print(f"My restaurant is {self.restaurant_name} and type of food is {self.cuisine_type}")

    def open_restaurant(self):
        print(f"{self.restaurant_name} is open at 12AM")

restaurant = Restaurant('Splecione', 'Polish' )
restaurant.describe_restaurant()
restaurant2 = Restaurant('Lane', 'English' )
restaurant2.describe_restaurant()
restaurant3 = Restaurant('Strucle', 'Italian' )
restaurant3.describe_restaurant()

# 9.3

class User():
    """present of user profile"""
    def __init__(self, first_name, last_name, e_mail, phone_number):
        self.first_name = first_name.title()
        self.last_name = last_name.title()
        self.e_mail = e_mail.title()
        self.phone_number = phone_number.title()

    def describe_user(self):
        print(f"\n{self.first_name} {self.last_name}")
        print(f"E-mail: {self.e_mail}")
        print(f"Phone number: {self.phone_number}")

    def greet_user(self):
        message = f"Hello {self.first_name} {self.last_name}"
        print(message)

user1 = User('Mark', 'Twain', 'mark@twain.com', '698574123')
user1.describe_user()
user1.greet_user()