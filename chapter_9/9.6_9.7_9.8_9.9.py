# 9.1 Ice cream stand

class Restaurant():
    """class about restaurant"""

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

class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name, cuisine_type = 'ice cream'):
        super().__init__(restaurant_name, cuisine_type)
        self.flavours = []

    def describe_flavours(self):
        print('Ice cream flavours: ')
        for flavour in self.flavours:
            print(f"{flavour.title()}")

ice = IceCreamStand('Frozen')
ice.flavours = ['mango', 'chocolate', 'vanilla', 'walnut']

ice.describe_restaurant()
ice.describe_flavours()

# 9.7 Admin
class User():
    """present of user profile"""
    def __init__(self, first_name, last_name, e_mail, phone_number):
        self.first_name = first_name.title()
        self.last_name = last_name.title()
        self.e_mail = e_mail
        self.phone_number = phone_number

    def describe_user(self):
        print(f"\n{self.first_name} {self.last_name}")
        print(f"E-mail: {self.e_mail}")
        print(f"Phone number: {self.phone_number}")

    def greet_user(self):
        message = f"Hello {self.first_name} {self.last_name}"
        print(message)

class Admin(User):
    """present of admin"""
    def __int__(self, first_name, last_name, e_mail, phone_number):
        super().__init__(first_name, last_name, e_mail, phone_number)
        self.privileges = []

    def show_privileges(self):
        print("Admin privileges:")
        for privilege in self.privileges:
            print(f"{privilege}")

jan = Admin('jan', 'nowak', 'janowak@up.com', 1254785245)
jan.describe_user()

jan.privileges = {
    '- addition of a post',
    '- deletion of post',
    '- ban a user',
    }

jan.show_privileges()

# 9.8
class User():
    """present of user profile"""
    def __init__(self, first_name, last_name, e_mail, phone_number):
        self.first_name = first_name.title()
        self.last_name = last_name.title()
        self.e_mail = e_mail
        self.phone_number = phone_number

    def describe_user(self):
        print(f"\n{self.first_name} {self.last_name}")
        print(f"E-mail: {self.e_mail}")
        print(f"Phone number: {self.phone_number}")

    def greet_user(self):
        message = f"Hello {self.first_name} {self.last_name}"
        print(message)

class Admin(User):
    """present of admin"""
    def __init__(self, first_name, last_name, e_mail, phone_number):
        super().__init__(first_name, last_name, e_mail, phone_number)
        self.privileges = Privileges()

class Privileges():

    def __init__(self, privileges = []):
        self.show_privileges = privileges

    def show_privileges(self):
        print("Admin privileges:")
        if self.privileges:
            for privilege in self.privileges:
                print(f"{privilege}")

    jan = Admin('jan', 'nowak', 'janowak@up.com', 1254785245)
    jan.describe_user()

    jan.privileges.show_privileges()

    jan_privileges = {
        '- addition of a post',
        '- deletion of post',
        '- ban a user',
        }
    jan.privileges.privileges = jan_privileges
    jan.privileges.show_privileges()
