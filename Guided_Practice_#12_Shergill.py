import formatting as f
import os

os.system("rm -r __pycache__")

f.title("Guided Practice #12")
f.dash()

print('--- Multiple Conditions ---\n')

requested_toppings=['mushrooms', 'extra cheese']

if 'mushrooms' in requested_toppings:
    print('adding mushrooms.')

if 'pepperoni' in requested_toppings:
    print('Adding pepperoni')

if 'extra cheese' in requested_toppings:
    print('Adding extra cheese.')

print('\nFinished making your pizza!\n')

requested_toppings=['mushrooms', 'extra cheese']

if 'mushrooms' in requested_toppings:
    print('adding mushrooms.')

elif 'pepperoni' in requested_toppings:
    print('Adding pepperoni')

elif 'extra cheese' in requested_toppings:
    print('Adding extra cheese.')

print('\nFinished making your pizza!')

print('\n--- Multiple Conditions ---\n')

x=10
y=10

if x<y:
    print('x is less than y')
elif x>y:
    print('x is greater than y')
else:
    print('x and y must be equal')

print('\n--- Nested IF Statements ---\n')

statement=0
statement1=0
statement2=0

if statement1:#outer if statement
    print('true')
    if nested_statement:#nested if statement
        print('yes')
    else:#nested else statement
        print('no')
else:#outer else statement
    print('false')

if statement1:#outer if
    print('hello world')
    if nested_statement1:#first nested if
        print('yes')
    elif nested_statement2:#first nested elif
        print('maybe')
    else:#first nested else
        print('no')
elif statement2:#outer elif
    print('hello galaxy')
    if nested_statement3:#second nested if
        print('yes')
    elif nested_statement4:#second nested elif
        print('maybe')
    else:#second nested else
        print('no')
else:#outer else
    statement('hello universe')

grade=int(input('Enter your grade: '))

if grade>= 65:
    print('Passing Grade of: ')
    if grade>=90:
        print('A')
    elif grade>=80:
        print('B')
    elif grade>=70:
        print('C')
    elif grade>=65:
        print('D')
else:
    print('Failing Grade')

if grade>=65:
    print('Passing grade of: ')
    if grade>=90:
        if grade > 96:
            print('A+')
        elif grade > 93 and grade<96:
            print("A")
        elif grade>=90:
            print("A-")
