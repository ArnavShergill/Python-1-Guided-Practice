print('\n---- Guided Practice #26 ----\n')

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

section('Tuple Basics')
subsection('Accessing Elements of a Tuple')

T=(13,5,92)
print(T[0])
print("The first element in the list is", T[0])

print(T[-1])
print(f"The last element in the list is {T[-1]}")

short_dash()
subsection('Converting a List into a Tuple')

L=[4,5.3,'name']
print(L)
print(type(L))

print()

T=tuple(L)
print(T)
print(type(T))

short_dash()
subsection('Converting a Tuple into a List')

T=('name', [2,4], 5.3, 19)
L=list(T)
print(L)
print(type(L))

short_dash()
subsection('Changing a Tuple Element')

T=(13,5,92)
print(T)

try:
    T[0]=5
except TypeError:
    print("\nError: Object does not support item assignment\n")

T=('name',[2,4],5.3,19)
print(f"Original List: {T}")

T[1][0]=5
print(f"Modified List: {T}")

short_dash()
subsection('Deleting a Tuple')

del(T)
try:
    print(type(T))
    print(T)
except NameError:
    print("Tuple has been deleted")

dash()
section('Creating Homogeneous Tuples')

T_int = (10,-4,59,58,23,50)
T_int_sorted=sorted(T_int)
print(T_int)
print(T_int_sorted)
print(type(T_int))

short_dash()

T_string = ("word", 'letter', 'vowel', 'spell', 'book', 'write', 'read')
T_string_sorted=sorted(T_string)
print(T_string)
print(T_string_sorted)
print(type(T_string))

short_dash()
subsection('Creating Heterogeneous Tuples')

T=('Tobias', 23, 25.3, [])
print(type(T))

T=((1.5,2.6), 'home', [5,96])
print(type(T))

short_dash()
subsection('Converting List to/from Tuples')

# List of student names
names_list=['Deepthi', 'Cassandra', 'Echo', 'Arlington', 'Kermit','Taylor','Trey','Bhanu','Ayush','Deephya']

#Sort the names alphabetically
sorted_list=sorted(names_list)

#Convert list into tuple
names_tuple=tuple(sorted_list)

#List converted into a tuple
print(type(names_tuple))

#Print the first and last name in that tuple
print("First name is: {:s}".format(names_tuple[0]))
print("Last name is: {:s}".format(names_tuple[-1]))

dash()
section("Creating Tuples from User Input")

#Collect 3 int numbers from a user
L=[]

for i in range(1,4):
    tmp=int(input("Enter an int{:d}/3: ".format(i)))
    L.append(tmp **2)

#Convert the list into a tuple
T=tuple(L)

#Print the content of the tuple
print("\nTuple of squares is : ", T, "\n")

#Prin teach fo the tuple elements on a new line
for i in range(3):
    print("T[{0:d}] = {1:d}".format(i, T[i]))

short_dash()
subsection('Changing Tuple Elements')

T=("Tobias", 23, 25.3, [])

#Tuples are immutable and cannot be changed.
try:
    T[0] = "Hello"
except:
    print("Error: Object does not support item assignment")

#A list inside a tuple can change
T[-1].append(44)

#The tuple did NOT change, it still refers to the same list; only the list was changed.
print(T)

dash()
