print('---- Guided Practice #21 ----\n')

import time

def section(section_name):
    print(f'--- {section_name} ---\n')

def dash():
    print('\n--------------------------------------------------------------------------------------------\n')

def short_dash():
    print('--------------------------------------\n')

section('Checking for Special Items')

requested_toppings = ['mushrooms', 'green peppers', 'extra cheese']

for requested_topping in requested_toppings:
    print(f"Adding {requested_topping}")

print('\nFinished making your pizza!\n')

short_dash()
time.sleep(1)

requested_toppings = ['mushrooms', 'green peppers', 'extra cheese']

for requested_toppings in requested_toppings:
    if requested_topping == 'green peppers':
        print("Sorry, we are out of green peppers right now.")
    else:
        print(f"Adding {requested_topping}.")

print("\nFinished making your pizza!")

dash()
time.sleep(3)
section('Checking That a List is Not Empty')

requested_toppings = []

if requested_toppings:
    for requested_topping in requested_toppings:
        print(f"Adding {requested_topping}.\n")
    print('\nFinished making your pizza!\n')
else:
    print('Are you sure you want a plain pizza?')

dash()
time.sleep(3)

section('Using Multiple Lists')

available_toppings = ['mushrooms', 'olives', 'green peppers', 'pepperoni', 'pineapple', 'extra cheese']

requested_toppings = ['mushrooms', 'french fries', 'extra cheese']

for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
        print(f"Adding {requested_topping}.\n")
    else:
        print(f"Sorry, we don't have {requested_topping}.\n")

print("Finished making your pizza!")

dash()
time.sleep(3)

