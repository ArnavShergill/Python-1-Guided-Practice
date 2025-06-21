from formatting import *

print("\n---- Guided Practice #38 ----\n")
section("Python Exception Handling")
subsection("Difference between Syntax Error and Exceptions")

# Initialize the amount variable
amount = 10000

#check that you are eligible to puchase DSA Self Paced or not
if(amount>2999):
    print("You are eligible to purchase DSA Self Paced")

short_dash()
subsection("Exceptions")

#initialize the amount varabile
marks = 10000

#perform division with 0
try:
    a = marks / 0
    print(a)
except ZeroDivisionError:
    print("Cannot divide by zero")

dash()
section("Try & Exception Statements")

#Python program to handle simple runtime error
#Python 3

a = [1, 2, 3]
try:
    print("Second element = %d" %(a[1]))

    #Throws error since there are only 3 elements in array
    print("fourth element = %d" %(a[3]))

except:
    print("An error occurred")

short_dash()
subsection("Catching Specific Exception")

def fun(a):
    if a < 4:

        #throws ZeroDivisionError for a = 3
        b = a/(a-3)

    #throws nameError if a >= 4
    print("Value of b = ", b)

try:
    fun(3)
    fun(5)

#note that braces () are necessary here for multiple exceptions
except ZeroDivisionError:
    print("ZeroDivisionError Occurred and Handled")
except NameError:
    print("NameError Occurred and Handled")

dash()
section("Try with Else Clause")

#Program to depict else clause with try-except
#Python 3
#function which returns a/b
def AbyB(a, b):
    try:
        c = ((a+b) / (a-b))
    except ZeroDivisionError:
        print("a/b resulted in 0")
    else:
        print(c)

#Driver program to test above function
AbyB(2.0, 3.0)
AbyB(3.0, 3.0)

short_dash()
subsection("Try-Except-Finally")

#Python program to demonstrate finally

#No exception Exception raised in try block
try:
    k = 5//0 #raises divide by zero exception.
    print(k)

#handles zerodivision exception
except ZeroDivisionError:
    print("Can't divide by zero")

finally:
    #This block is always executed regardless of exception generation
    print("This is always executed")

short_dash()
subsection("Try-Except-Else-Finally")

try:
    #Get user input
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))

    #Perform the division
    result = numerator / denominator

except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")

except ValueError:
    print("Error: Invalid input. Please enter integers only.")

else:
    #Code to be executed of no exception occurs
    print("The result of the division is:", result)

finally:
    #Code that will always be executed, regardless of exceptions
    print("Program execution complete.")

dash()
section("Nested Exceptions")

def fun(a):
    if a < 4:
        b=a/(a-3)
        print("Value of b=", b)

try:
    fun(5)
except ZeroDivisionError:
    print("ZDE")
except NameError:
    print("NEO")
else:
    try:
        fun(3)
    except ZeroDivisionError:
        print("ZDE")
    except NameError:
        print("NEO")

dash()
section("Raising Exception")

#Program to depict Raising Exception

x = 'Hello'

if not type(x) is int:
    raise TypeError("Only integers are allowed")

x = -1

if x < 0:
    raise Exception("Sorry, no numbers below zero")

dash()
