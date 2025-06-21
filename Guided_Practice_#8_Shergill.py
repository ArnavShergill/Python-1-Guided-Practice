import formatting as f
import os

os.system("rm -r __pycache__")

f.title("Guided Practice #8")
f.dash()

print('---- Guided Practice #8 ----\n')
print('--- Positional Arguments ---\n')

def describe_pet(animal_type, pet_name):
    """display information about a pet."""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}")

describe_pet('hamster', 'harry')

print('\n--- Multiple Function Cells ---\n')

def describe_pet(animal_type, pet_name):
    """display information about a pet."""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}")

describe_pet('hamster', 'harry')
describe_pet('dog','willie')

print('\n--- Order Matters ---\n')

def describe_pet(animal_type, pet_name):
    """display information about a pet."""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}")

describe_pet('harry','hamster')

print('\n--- Keywords ---')

def describe_pet(animal_type, pet_name):
    """display information about a pet."""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}")

describe_pet(animal_type='hamster', pet_name='harry')

print('\n--- Default Values ---')

def describe_pet(pet_name, animal_type='dog'):
    """display information about a pet."""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}")

describe_pet(pet_name='willie')
describe_pet('willie')
describe_pet(pet_name='harry', animal_type='hamster')
