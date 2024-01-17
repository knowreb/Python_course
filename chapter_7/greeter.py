name = input("State your name: ")
print(f"Hello, {name}!")

prompt = "If you tell us who you are we will personalise the message displayed."
prompt += "\nWhat is your name? "

name = input(prompt)
print(f"\nHello, {name}!")

# page199 using function with loop while
def get_formatted_name(first_name, last_name):
    """Returns an elegantly formatted name."""
    full_name = f"{first_name} {last_name}"
    return full_name.title()

# this is a loop runing indefinitely
while True:
    print("\nPlease state your first name i last name :")
    f_name = input('First name: ')
    l_name = input('Last name:')

    formatted_name = get_formatted_name(f_name, l_name)
    print(f"\nHello, {formatted_name}!")

# use of the break function to leave the loop
def get_formatted_name(first_name, last_name):
    """Returns an elegantly formatted name."""
    full_name = f"{first_name} {last_name}"
    return full_name.title()

while True:
    print("\nPlease state your first name i last name :")
    print("(type 'q', to quit at any time)")

    f_name = input('First name: ')
    if f_name == 'q':
        break
    l_name = input('Last name:')
    if l_name == 'q':
        break
    formatted_name = get_formated_name(f_name, l_name)
    print(f"\nHello, {formatted_name}")

    formatted_name = get_formatted_name(f_name, l_name)
    print(f"\nHello, {formatted_name}!")