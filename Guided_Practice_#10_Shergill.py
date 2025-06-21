import formatting as f
import os

os.system("rm -r __pycache__")

f.title("Guided Practice #10")
f.dash()

print('--- Checking for Equality ---\n')

car = 'BMW'
print(car=='BMW')

car = 'Audi'
print(car=='BMW')

print('\n--- Checking for Equality ---\n')

car = 'Audi'
print(car=='audi')

print(car.lower()=='audi')
print(car)

print('\n--- Checking for Inequality ---\n')

requested_topping = 'mushrooms'

if requested_topping != 'anchovies':
    print('Hold the anchovies!')

print('\n--- Numerical Comparisons ---\n')

age=18
print(age==18)

answer=17

if answer != 42:
    print('That is not the correct answer. Please try again')

age=19
print(age<21)

print(age<=21)
print(age>21)
print(age>=21)

print('\n--- Using And ---\n')

age0=19
age1=22
print(age0==21 and age1>=21)

age0=22
age1=18
print(age0>=21 and age1==21)

age1=22
print(age0>=21 and age1 >=21)

print((age0>=21) and (age1 >= 21))

print('\n--- Using or ---\n')

age0=22
age1=18
print((age0>=21) or (age1>=21))

age0=18
print((age0>=21) or (age1 >= 21))
