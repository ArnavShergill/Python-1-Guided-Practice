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

print('\n---- Guided Practice #28 ----\n')

section('Tuple Operations & Functions')
subsection("Containment (In, Not In)")

T = (4, [5,6], 'name', 3.5, True)

print("4 contained in T?", 4 in T)
print("5 not contained in T?", 5 not in T)
print("False contained in T?", False in T)

short_dash()
subsection('Using Containment in an IF Statement')

#Create a tuple
my_tuple=(1, 2, 3, 4, 5)

#Test if a value is in the tuple
if 3 in my_tuple:
    print("3 is in the tuple")
else:
    print("3 is not in the tuple")

#Test if a value is not in the tuple
if 6 not in my_tuple:
    print("6 is not in the tuple")
else:
    print("6 is in the tuple")

short_dash()
subsection('Identity (is) and equality (==)')

#Equivalent tuples, not identical
T1 = (10, [2,4], 59)
T2 = (10, [2,4], 59)

if (T1 == T2):
    print("Equal tuples")
else:
    print("Not equal tuples")

if (T1 is T2):
    print("Identical Tuples")
else:
    print("Not identical tuples")


#Identical tuples (also equivalent)
T1 = (10, [2,4], 59)
T2 = T1

if (T1 == T2):
    print("Equal tuples")
else:
    print("Not equal tuples")

if (T1 is T2):
    print("Identical Tuples")
else:
    print("Not identical tuples")

#Changing one of 2 identical tuples
T1 = (10, [2,4], 59)
T2 = T1

#A change in T1 is a change in T2
T1[1][0] = 20

print("T1 = ", T1)
print("T2 = ", T2)

short_dash()
subsection("Concatenation")

T1 = ("First", "Last")
T2 = ("Middle",) #single element tuple

#Concatenate two tuples
T = T1 + T2
print(T)

T1 = (10, [2, 4], 59)
T2 = (10, [2, 4], 'name', 3.5, True)

#Concatenate sliced tuples
T = T1[1:] + T2[0:2]
print(T)

short_dash()
subsection("Length of a Tuple (len)")

#length of tuple
T1 = (10, [2,4], 59)
print(len(T1))

#Iterate over elements of a tuple
T1 = (10, [2,4], 59)

for i in range(len(T1)):
    print("T1[{:d}] = {}".format(i, T1[i]))

dash()
section("List Containment Examples")
subsection('1')

fruits=['apple','banana','orange']
if 'apple' in fruits:
    print("Yes, apple is present in the list")
else:
    print('No, apple is not present in the list')

short_dash()
subsection('2')

fruits=['apple','banana','orange']
if 'mango' not in fruits:
    print("Yes, mango is not present in the list")
else:
    print('No, mango is present in the list')

short_dash()
subsection('3')

fruits=['apple','banana','orange']
index=fruits.index('banana')
print('The index of banana is:', index)

dash()
