import time

def section(section_name):
    print(f'--- {section_name} ---\n')

def subsection(section_name):
    print(f'-- {section_name} --\n')

def dash():
    print('\n--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------\n')
    time.sleep(3)

def short_dash():
    print('\n----------------------\n')
    time.sleep(1)

def list_format(list_name):
    print(", ".join(list_name))

def list_format_sorted(list_name):
    print(", ".join(sorted(list_name)))

print('\n---- Guided Practice #27 ----\n')

T=('name', [2,4], 5.3,19)

# From index 1 (included) to index 2 (excluded)
print(T[1:2])

#From index 1 (included) to the last element.
print(T[1:])

# From the start of a tuple to index 2 (excluded)
print(T[:2])

# From index -3 (included) to index -1 (excluded)
print(T[-3:-1])

# From index -3 to the last element
print(T[-3:])

# All elements
print(T[:])

dash()
section("Slicing Tuples Examples")

T = (12 ,24, 'name', 'city')

#Slice the tuple into numerical and textual tuples
numerical_tuple = T[0:2]
print(numerical_tuple)

textual_tuple = T[-2:]
print(textual_tuple)

dash()
section('Unpacking Tuples')

a, b = (4, 5)

print(f"First item unpacked: {a}")
print(f"Second item unpacked : {b}")

short_dash()

x, y, z = 1, 2, 3

print(f'First item unpacked: {x}')
print(f'Second item unpacked: {y}')
print(f'Third item unpacked: {z}')

dash()
section("Unpacking Tuples Examples")

subsection('Example 1')
#Swap variables using tuple unpacking
e1=5
e2=109
print("\nBefore swapping: ")
print("e1 = {:3d}\ne2 = {:3d}".format(e1, e2))

short_dash()
subsection('Example 2')

#Define a tuple
my_tuple=(1, 2, 3)

#Unpack the tuple into individual variables
a, b, c = my_tuple

#Print out the variables
print(a)#Output: 1
print(b)#Output: 2
print(c)#Output: 3

short_dash()
subsection('Example 3')

#Define a list of tuples
my_list=[(1,2), (3,4), (5,6)]

#Loop through the list and unpack each tuple into individual variables
for a, b in my_list:
    print(a+b)

short_dash()
subsection('Example 4')

#Define a tuple with four elements
my_tuple=(1, 2, 3, 4)

#Unpack the firs ttwo elements of the tuple into variables a and b, and the rest of the elements into a list c
a, b, *c = my_tuple

#Print out the variables
print(a) #Output: 1
print(b) #Output: 2
print(c) #Output: [3, 4]

dash()
section('Returning Function Values')

# Split a full name into the first and last names
def split_name(name):
    names = name.split(" ")
    first_name = names[0]
    last_name = names[-1]
    #Pack th evariable into a tuple, then return the tuple
    return(first_name, last_name)

#ask user for input
name = input("Enter your full name: ")

#Unpack the returned tuples into first, last variables
#looks like th efunction returns 2 variables
first, last = split_name(name)

#Unpacked variables can be used separately
print("First name: {:s}".format(first))
print("Last name: {:s}".format(last))

short_dash()
section("Another Way")

def split_name(full_name):
    first_name, last_name = full_name.split()
    return first_name, last_name

#call the function and unpack the returned tuple into separate variables
first_name, last_name = split_name(input("Enter your full name: "))

#Print out the variables
print("First Name:",first_name)# Output: "John"
print("Last Name:",last_name)# Output: "Smith"

dash()
