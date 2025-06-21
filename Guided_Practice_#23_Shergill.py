print('\n---- Guided Practice #23 ----\n')

import time

def section(section_name):
    print(f'--- {section_name} ---\n')

def dash():
    print('\n--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------\n')
    time.sleep(3)

def short_dash():
    print('\n----------------------\n')
    time.sleep(1)

section('Passing a List')

def greet_users(names):
    """Print a simple greeting to each user in the list."""
    for name in names:
        msg=f"Hello, {name.title()}!"
        print(msg)

usernames=['hannah', 'ty', 'margot']
greet_users(usernames)

dash()
section('Modifying a List in a Function')

#Start with some designs that need to be printed.

unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
completed_models = []

#Simulate printing each design, until none are left.
#Move each design to completed_models after printing.

while unprinted_designs:
    current_design = unprinted_designs.pop()
    print(f"printing model: {current_design}")
    completed_models.append(current_design)

#Display all completed models.
print("\nThe following models have been printed: ")
for completed_model in completed_models:
    print(completed_model)

short_dash()

def print_models(unprinted_designs, completed_models):
    """
    Simulate printing each design, until none are left.
    Move each design to completed_models after printing.
    """

    while unprinted_designs:
        current_design = unprinted_designs.pop()
        print(f"Printing Model: {current_design}")
        completed_models.append(current_design)

def show_completed_models(completed_models):
    """Show all the models that were printed."""
    print("\nThe following models have been printed: ")
    for completed_model in completed_models:
        print(completed_model)

unprinted_designs=['phone case', 'robot pendant', 'dodecahedron']
completed_models=[]

print_models(unprinted_designs, completed_models)
show_completed_models(completed_models)

dash()

section('Preventing a Function From Modifying a List')

print_models(unprinted_designs[:], completed_models)

dash()
