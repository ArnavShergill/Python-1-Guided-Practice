import formatting as f
import os

os.system("rm -r __pycache__")

f.title("Guided Practice #15")
f.dash()

f.section('% Formatter')

name=input("What is your name? ")
age=int(input('What is your age? '))

print('\nHi, my name is %s, and I am %d years old.' % (name, age))

favorite_subject=input('\nWhat is your favorite subject? ')

print('\nMy favorite sebject is %s.' % favorite_subject)

f.section('Str.Format() Method')

print('Sammy has {} balloons.'.format(5))

def dash():
    print('\n---------------\n')

dash()

open_string='Sammy loves {}.'
print(open_string.format('open source'))
dash()

f.section('Using Formatters with Multiple Placehoders')

new_open_string='Sammy loves {} {}' #2 {} placeholders
print(new_open_string.format('open source', 'software')) #Pass 2 strings into method, seperated by a comma

dash()

sammy_string='Sammy loves {} {}, and has {} {}.'
print(sammy_string.format('open-source', 'software', 5, 'balloons'))

f.section('Reordering Formatters')

print('Sammy the {} has a pet {}!'.format('shark', 'pilot fish'))
dash()

print('Sammy the {0} has a pet {1}'.format('shark','pilot fish'))
print('Sammy the {1} has a pet {0}'.format('shark','pilot fish'))

f.section('Specifying Type')

print('Sammy ate {0:f} percent of a {1}!'.format (75, 'pizza'))
dash()

print('Sammy ate {0:.3f} percent of a pizza!'.format(75.765376))
dash()
print('Sammy ate {0:1f} percent of a pizza!'.format(75.765376))
dash()
print('Sammy ate {0:.0f} percent of a pizza!'.format(75.765376))

f.section('Using Variables')

nBalloons=8
print('Sammy has ballons today!'.format(nBalloons))
dash()

sammy="Sammy has {} balloons today!"
nBalloons=8
print(sammy.format(nBalloons))
dash()

f.section('Padding Variable Substitutions')

print('Sammy has  {0:5} red {1:16}!'.format(5, 'balloons'))
dash()

print('Sammy has {0:<4} red {1:^16}!'.format(5, 'balloons'))
dash()

print('{:*20s}'.format("Sammy"))
dash()

print("Sammy ate {0:5.0f} percent of a pizza!".format(75.765376))

f.section('Using Formatters to Organize Data')

for i in range(3,13):
    print (i, i*i, i*i*i)

dash()

for i in range(3,13):
    print("{:3d} {:4d} {:5d}".format(i, i*i, i*i*i))

dash()

for i in range(3,13):
    print('{:6d}{:6d}{:6d}'.format(i, i*i, i*i*i))
