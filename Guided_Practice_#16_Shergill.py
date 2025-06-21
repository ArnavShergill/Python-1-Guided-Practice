print('---- Guided Practice #16 ----\n')

import time

def section(section_name):
    print(f'--- {section_name} ---\n')

def seconds(lasting=3):
    time.sleep(lasting)
    
def dash():
    print('\n------------------------------------------------------\n')

section('Accessing Elements in a List')

bicycles=['trek', 'cannondale', 'redline', 'specialized']
print(bicycles[0].title())

dash()
seconds(3)

section('Index Positions')

print(bicycles[1])
print(bicycles[3])
print(bicycles[-1])

dash()
seconds(3)

section('Using Individual Values')

message= f'My first bicycle was a {bicycles[0].title()}'

print(message)

dash()
seconds(4)

section('Read in a List')

sales=[]

for count in range (1, 11):
    prompt=input('Enter the sales for Stand'+str(count)+': ')
    if prompt !='quit':
        sales.append(prompt)
    if prompt=='quit':
        break

print(sales)

dash()
seconds(3)

section('Enumerate Function')

# List of Friends
friends = ['Alice', 'Bob', 'Charlie', 'Dana', 'Eli']

#Using enumerate() in a for loop
for index, name in enumerate(friends):
    print(f"{index}: {name.title()}")

dash()
