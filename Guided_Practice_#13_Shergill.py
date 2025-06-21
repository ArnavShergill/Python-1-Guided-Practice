import formatting as f
import os

os.system("rm -r __pycache__")

f.title("Guided Practice #13")
f.dash()

print('--- Introducing While Loops --- \n')

current_number = 1

while current_number<=5:
    print(current_number)
    current_number+=1

print('\n--- Letting the User Choose When to Quit ---')

prompt = '\nTell me something, and I will repeat it back to you'
prompt += '\nEnter \'quit\' to end the program: '
message = ''

while message != 'quit':
    message=input(prompt)
    if message!='quit':
        print(message)

print('\n--- Using a Flag ---')

prompt = '\nTell me something and I will repeat it abck to you: '
prompt += '\nEnter \'quit\' to end the program. '

active = True
while active:
    message=input(prompt)
    if message=='quit':
        active=False
    else:
        print(message)

print('\n--- Using Break to Exit a Loop ---')

prompt = '\nPlease enter the name of a city you have visited: '
prompt += '\n(Enter \'quit\' when you are finished): '

while True:
    city = input(prompt)
    if city =='quit':
        break
    else:
        print(f'I\'d love to go to {city.title()}!')

print('\n--- Using Continue in a Loop ---')

current_number=0
while current_number < 10:
    current_number+=1
    if current_number%2 ==0:
        continue
    print(current_number)

print('\n--- Avoiding Infinite Loops ---\n')

x=1
while x<=5:
    print(x)
    x+=1

print('\n--- FOR Loop Construction ---\n')

names = ('Rob', 'Mary', 'David', 'Jenny', 'Chris', 'Imogen')
for name in names:
    print(name)

#Times Table Loops
times_value = 2
for count in range(1, 13):
    result=count*times_value
    print(count, 'times', times_value, 'equals', result)

print('\n--- For Loop Syntax ---\n')

word = input('Type a word: ')
for letter in word:
    print(letter)

print('\n--- Using a Function with a While Loop ---\n')

def get_formatted_name(first_name, last_name):
    '''return a full name, neatly formatted'''
    full_name=f'{first_name} {last_name}'
    return full_name.title()

#This is an infinite loop!
while True:
    print('\nPlease tell me your name: ')
    f_name=input('First name: ')
    if f_name == 'q':
        break
    l_name=input('Last name: ')
    if l_name=='q':
        break
    formatted_name=get_formatted_name(f_name,l_name)
    print(f'\nHello, {formatted_name}!')
