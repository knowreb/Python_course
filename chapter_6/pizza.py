#storage of information about the pizza ordered by the customer
pizza = {
    'crust': 'thick',
    'toppings': ['muchrooms', 'double cheese'],
    }

# podsumowanie zamowienia
print(f"You ordered a {pizza['crust']} pizza")

for topping in pizza['toppings']:
    print(f"\t{topping}")


# Forwarding an arbitrary number of arguments (p205)
def make_pizza(toppings):
    """Display the list of additives selected by the customer"""
    print(toppings)
make_pizza('pepperoni')
make_pizza('muchrooms', 'green pepper', 'double cheese')

def make_pizza(toppings):
    """summary information on the prepared pizza"""
    print("\nI prepare a pizza with the following ingredients:")
    for topping in toppings:
        print(f" - {topping}")

    make_pizza('pepperoni')
    make_pizza('mushrooms', 'green pepper', 'double cheese')
