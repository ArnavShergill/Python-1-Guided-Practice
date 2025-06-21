import formatting as f
import os

os.system("rm -r __pycache__")

f.title("Guided Practice #11")
f.dash()

print('--- Simple IF Statements ---\n')

hour=8

if hour> 6:
    print('It is time to get up!')
    print('The early Bird Gets the Worm!')

if hour>6: print('IT IS TIME TO GET UP');print('THE EARLY BIRD GETS THE WORM')

print('\n--- If Statements ---\n')

age=19
if age>=18:
    print('You are old enough to vote!')
    print('Have you registered to vote yet? ')

print('\n--- If/Else Statements ---\n')

age=17

if age>=18:
    print('You are old enough to vote!')
    input('Have you registered to vote yet? ')
else:
    print("Sorry, you are too young to vote.")
    print('Please register to vote as soon as you turn 18!')

print('\n--- If/Elif/Else Statements ---\n')

age=4

if age<4:
    print('Your admission cost is $0.')
elif age<18:
    print('Your admission cost is $25.')
else:
    print('Your admission cost is $40.')

age=12

if age<4:
    price=0
elif age<18:
    price = 25
else:
    price=40

print(f'Your admission cost is ${price}.')

print('\n--- Multiple Elif Statements ---\n')

age=12

if age<4:
    price=0
elif age<18:
    price=25
elif age<65:
    price=40
else:
    price=20

print(f'Your admission cost is ${price}.')

age=12

if age<4:
    price=0
elif age<18:
    price = 25
elif age<65:
    price=40
elif age>=65:
    price=20

print(f'Your admission cost is ${price}.')

print('\n--- Nesting IF Statements ---\n')

#Greeter with Password

name=input('Enter your name: ')

if name.upper() == 'ROB':
    password=input('Enter the password: ')
    if password == 'secret':
        print('Hello, Oh Great One!')
    else:
        print('Begone, Imposter')

name=input('Enter your name: ')

if name.upper() == 'ROB':
    password=input('Enter the password: ')
    if password == 'secret':
        print('Hello, Oh Great One!')
    else:
        print('Begone, Imposter')
else:
    print('You are not Rob. SHAME.')
