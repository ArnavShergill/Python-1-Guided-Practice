print('---- Guided Practice #20 ----\n')

def section(section_name):
    print(f'--- {section_name} ---\n')

def dash():
    print('\n--------------------------------------------------------------------------\n')

def short_dash():
    print('----------------------------\n')

section('Slicing a List')

players=['Spoorthi', 'Kelly', 'Yakaira', 'Ariana', 'Marcella', 'Rachel']

print(players[0:3], '\n')
short_dash()
print(players[1:4], '\n')
short_dash()
print(players[:4], '\n')
short_dash()
print(players[2:], '\n')
short_dash()
print(players[-3:])
dash()

section('Slicing Through a FOR Loop')

players=['eric', 'caden', 'jack', 'nathan', 'bhargava', 'aidan']

print('Here are the first three players on my team: \n')
for player in players[:3]:
    print(player.title(), '\n')
dash()

section('Slicing through a WHILE Loop')

my_list=list(range(1,6))
start_index=0
end_index=3

while start_index<end_index:
    print(my_list[start_index], '\n')
    start_index+=1
dash()

section('Copying a List')

my_foods=['pizza', 'CORN', 'beets']
friend_foods=my_foods[ : ]

print('My favorite foods are: ')
print(my_foods, '\n')
short_dash()
print('My friend\'s favorite foods are: ')
print(friend_foods, '\n')
short_dash()

my_foods=['pizza', 'CORN', 'beets']
friend_foods = my_foods[ : ]

my_foods.append('Chinese')
friend_foods.append('frogs')

print('My favorite foods are: ')
print(my_foods, '\n')
short_dash()
print('My friend\'s favorite foods are: ')
print(friend_foods, '\n')
short_dash()

#This doesn't work:

my_foods=['pizza', 'CORN', 'beets']
friend_foods = my_foods

my_foods.append('Chinese')
friend_foods.append('frogs')

print('My favorite foods are: ')
print(my_foods, '\n')
short_dash()
print('My friend\'s favorite foods are: ')
print(friend_foods, '\n')
short_dash()
