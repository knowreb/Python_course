pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']
print(pets)

while 'cat' in pets:
    pets.remove('cat')

print(pets)

#page188

def describe_pet(animal_type, pet_name):
    """describ information about the animal."""
    print(f"My animal is: {animal_type}.")
    print(f"My {animal_type} name is {pet_name.title()}.")

describe_pet('dog', 'Daisy')

