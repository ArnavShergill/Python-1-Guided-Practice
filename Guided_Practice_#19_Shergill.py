print('---- Guided Practice #19 ----\n')

def section(section_name):
    print(f'--- {section_name} ---\n')

def dash():
    print('\n---------------------------------------------------------------------------------\n')

def short_dash():
    print('\n------------------------------\n')

section('Using the range() Function')

for value in range(1,5):
    print(value)

short_dash()

for value in range(1, 6):
    print(value)

dash()

section('Using range() to Make a List of Numbers')

numbers=list(range(1,6))
print(numbers)

short_dash()

even_numbers=list(range(2, 11, 2))
print(even_numbers)

short_dash()

squares=[]
for value in range(1,11):
    square = value ** 2
    squares.append(square)

print(squares)

short_dash()

squares=[]
for value in range(1,11):
    squares.append(value**2)

print(squares)

dash()

section('Simple Statistics with List of Numbers')

digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
print(min(digits))
print(max(digits))
print(sum(digits))

short_dash()

squares=[value ** 2 for value in range(1,11)]
print(squares)

dash()
