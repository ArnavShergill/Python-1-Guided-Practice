import formatting as f
import os

os.system("rm -r __pycache__")

f.title("Guided Practice #3")
print('--- Intro ---\n')
print(True)
f_bool=False
print(f_bool)
print('\n--- is alpha ---\n')
message="let's test out booleans"
print(message.isalpha())
message='3'
print(message.isalpha())
print('\n--- is all num ---\n')
example='abc 123'
print(example, "is alphanumeric?", example.isalnum())
example="abc_123"
print(example, "is alphanumeric?", example.isalnum())
example='000'
print(example, "is alphanumeric?", example.isalnum())
example='aaaa'
print(example, "is alphanumeric?", example.isalnum())
print('\n--- is title ---\n')
message='a cold stormy night'
print(message.istitle())
message='welcome to the jungle'
print(message.istitle())
print('\n--- is digit ---\n')
#checking for digit
example='15460'
print(example.isdigit())
example='154ayush60'
print(example.isdigit())
print('\n--- is slower/upper ---\n')
#checking for uppercase characters
example='ECHOTHEDOLPHIN'
print(example.isupper())
example='SonicTheHedgehog'
print(example.isupper())
example='crazytaxi'
print(example.islower())
example='SonicSpinball'
print(example.islower())
print('\n--- starts with ---\n')
#Python code to implement startswith()
string='HaloReach'
print(string.startswith('Halo'))
print('\n--- Printing Type Functions ---\n')
print(type('This is a string'))
print(type(10.23))
print(type(100))
print('\n--- Variables in Type Functions ---\n')
string='This is a string'
decimal = 10.23
integer = 100
print(type(string))
print(type(decimal))
print(type(integer))
