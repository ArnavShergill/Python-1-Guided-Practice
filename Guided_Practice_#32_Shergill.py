import time

def section(section_name):
    print(f'--- {section_name} ---\n')

def subsection(section_name):
    print(f'-- {section_name} --\n')

def dash():
    print('\n--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------\n')
    time.sleep(3)

def short_dash():
    print('\n----------------------\n')
    time.sleep(1)

def list_format(list_name):
    print(", ".join(list_name))

def list_format_sorted(list_name):
    print(", ".join(sorted(list_name)))

print("\n---- Guided Practice #32 ----\n")

section("Passing an Arbitrary Number of Arguments")
subsection("Arguments")

def build_pizza(*toppings):
    """Print the list of toppings that have been requested."""
    print(toppings)

#Calling the function with different numbers of arguments
build_pizza('pepperoni')
build_pizza('mushrooms', 'green peppers', 'extra cheese')

subsection("Enanced Arguments")

def build_pizza(*toppings):
    """Print the list of toppings that have been requested."""
    print("Making a pizza with the following toppings:")
    for topping in toppings:
        print(f"- {topping}")

# Calling the function with different numbers of arguments
build_pizza('pepperoni')
build_pizza('mushrooms', 'green peppers', 'extra cheese')

dash()
section("Mixing Positional & Arbitrary Arguments")
subsection("Mixing Arguments")

def make_pizza(size, *toppings):
    """Summarize the pizza we are about to make."""
    print(f"Making a {size}-inch pizza with the following toppings:")
    for topping in toppings:
        print(f"- {topping}")

#Calling the function
make_pizza(16, 'pepperoni')
make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')

dash()
section("Using Arbitrary Keyword Arguments")
subsection("Keyword Arguments")

def build_profile(first_name, last_name, **user_info):
    profile={}
    profile['first_name'] = first_name
    profile['last_name'] = last_name
    for key, value in user_info.items():
        profile[key] = value
    return profile

user_profile = build_profile('albert', 'einstein',  location='Princeton', field='Physics')
print(user_profile)

dash()
