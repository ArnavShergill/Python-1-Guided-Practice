print('\n---- Guided Practice #24 ----\n')

import time

def section(section_name):
    """It's easier to make a function that will format the print line for me so that I only have to do it once and use it for all of the sections."""
    print(f'--- {section_name} ---\n')

def dash():
    """This is used to seperate the sections."""
    print('\n--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------\n')
    time.sleep(3)

def short_dash():
    """This is used to seperate blocks of code within a section and blocks of output within the shell."""
    print('\n----------------------\n')
    time.sleep(1)

section('The sort() Method')

cars=['bmw','audi','toyota','subaru']
cars.sort()
print(cars)

short_dash()

cars=['bmw','audi','toyota','subaru']
cars.sort(reverse=True)
print(cars)

dash()
section('Sorting a List Temporarily')

cars=['bmw','audi','toyota','subaru']

print("Here is the original list: ")
print(cars)
short_dash()
print('Here is the sorted list: ')
print(sorted(cars))
short_dash()
print("Here is the original list again: ")
print(cars)

dash()
section('Sorted() Function')

game_points=[3, 14, 0, 8, 21, 1, 3, 8]
sorted_points=sorted(game_points)
print(game_points)
print(sorted_points)

short_dash()

x=[2, 8, 1, 4, 6, 3, 7]

print("Sorted List Returned: ", sorted(x))
print("\nReverse Sort: ", sorted(x, reverse=True))
print("\nOriginal List Not Modified: ", x)

short_dash()

x='python'
print(sorted(x))

dash()
section('Print a List in Reverse Order')

cars=['bmw','audi','toyota','subaru']
print(cars)

cars.reverse()
print(cars)

dash()
section('Find the Length of a List')

cars=['bmw','audi','toyota','subaru']
print(len(cars))

dash()
section('.extend() List Method')

example1=[1, 2, 3]
example1.extend([4, 5, 6])
print(example1)

short_dash()

example1=[1, 2, 3]
example2=[4, 5, 6]
example1.extend(example2)

print(example1)

dash()
section('.join List Method')

cars=['bmw','audi','toyota','subaru']
print("Original List Ascending: ", ", ".join(sorted(cars)))
print("Original List Descending: ", ", ".join(sorted(cars, reverse=True)))
