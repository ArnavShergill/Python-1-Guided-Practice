import time

def section(section_name):
    print(f'--- {section_name} ---\n')

def subsection(section_name):
    print(f'-- {section_name} --\n')

def dash():
    print('\n------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------\n')
    time.sleep(3)

def short_dash():
    print('\n----------------------\n')
    time.sleep(1)

def list_format(list_name):
    print(", ".join(list_name))

def list_format_sorted(list_name):
    print(", ".join(sorted(list_name)))

print("\n---- Guided Practice #31 ----\n")
section("Pass Statements")

#Does nothing, but syntactically valid
def useless_function():
    pass

#Does nothing, but syntactically valid
for i in range(10):
    pass

#Does nothing, but syntactically valid
if (5<6):
    pass

dash()
section("Nested Loops")
subsection("Displaying a Table")

#list of lists
table = [[5, 2, 6], [4, 6, 0], [9, 1, 8], [7, 3, 8]]

for row in table:
    for col in row:
        #print the value col followed by a tab
        print(col, end = '\t')

    #Print a new line
    print()

subsection("Character Art")

def char_art(steps):
    for row in range(steps):
        for col in range(steps):
            if (col <= row):
                print("[]", end = "")
        print()

#Generate a staircase with 6 steps
char_art(6)

dash()
section("Loops Containing Compound Conditional Expressions")
subsection("Largest Even Number")

lst=[102, 34, 55, 166, 20, 67, 305]

#Nesting a compound conditional in a for loop

largest = 0

for num in lst:
    #Test if num is even and greater than largest
    if ((largest < num) and (num % 2 ==0)):
        largest=num

print("Largest even number in the list is: ", largest)

short_dash()
subsection("Counting Within Ranges")

#Ages of 100 people
ages = (86, 38, 30, 19, 29, 6, 95, 22, 23, 82, 39, 73, 30, 98, 5, 68, 57, 34, 35, 81, 54, 77, 29, 75, 83, 14, 88, 7, 8, 32, 93, 76, 42, 1, 32, 70, 70, 3, 34, 52, 44, 41, 7, 77, 73, 97, 34, 13, 33, 54, 8, 82, 21, 55, 72, 41, 34, 98, 72, 73, 24, 55, 50, 63, 38, 92, 43, 68, 52, 68, 69, 51, 19, 24, 35, 55, 74, 47, 8, 19, 69, 12, 96, 96, 11, 30, 97, 73, 22, 25, 19, 85, 37, 68, 39, 76, 73, 18, 45, 42)

#Initial count
children = 0
teens = 0
young_adults = 0
adults = 0

#Neseting compound conditionals within a for loop
for age in ages:
    if(age <= 12):
        children += 1
    elif ((age>13) and (age <=19)):
        teens += 1
    elif ((age >20) and (age <= 30)):
        young_adults += 1
    elif (age>30):
        adults += 1

print("Number of children:", children)
print("Number of teens:", teens)
print("Number of young adults:", young_adults)
print("Number of adults:", adults)

dash()
