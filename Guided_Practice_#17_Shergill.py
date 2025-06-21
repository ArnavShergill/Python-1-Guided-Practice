print('---- Guided Practice #17 ----\n')
def section(section_name):
    print(f'--- {section_name} ---\n')

def dash():
    print('\n------------------------------------------------------\n')

section('Modifying a List Introduction')

motercycles = ['honda', 'yamaha', 'suzuki']
print(motercycles)

motercycles[0]='ducati'
print(motercycles)

dash()

section('Adding Elements to a List')

motorcycles=[]

motorcycles.append('honda')
motorcycles.append('yamaha')
motorcycles.append('suzuki')

print(motorcycles)
dash()

motercycles=['honda', 'yamaha', 'suzuki']

motorcycles.insert(0,'ducati')
print(motorcycles)

dash()

section('Removing Elements from a List')

motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

del motorcycles[0]
print(motorcycles)

del motorcycles[1]
print(motorcycles)

dash()

section('Using the pop() Method')

motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

popped_motorcycle=motorcycles.pop()
print(motorcycles)
print(popped_motorcycle)

motorcycles = ['honda', 'yamaha', 'suzuki']

last_owned = motorcycles.pop()
print(f'The last motorcycle I owned was a {last_owned.title()}.')

dash()

section('Popping Items from any Position')

motorcycles=['honda', 'yamaha', 'suzuki']

first_owned=motorcycles.pop(0)
print(f'The first motorcycle I owned was a {first_owned.title()}.')

dash()

section('Removing an Item by Value')

motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
print(motorcycles)

motorcycles.remove('ducati')
print(motorcycles)

dash()

motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
print(motorcycles)

too_expensive = 'ducati'
motorcycles.remove(too_expensive)
print(motorcycles)
print(f'\nA {too_expensive.title()} is too expenive for me.')

dash()
