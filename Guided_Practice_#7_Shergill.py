import formatting as f
import os

os.system("rm -r __pycache__")

f.title("Guided Practice #7")
f.dash()

num1=5
num2=9
num3=num1+num2

"""Returns the sum of
num1 & num2"""

print(num3)

"""
docstrings won't show

the docstrings will not show in the shell if we don't want it to.
"""

print('\n--- Functions ---\n')
#A simple Python Function
def fun():
    """This function prints a message welcoming the students to class"""
    print("Welcome to Python 1: Honors")

fun()

print('\n--- Defining a Function ---\n')
def greet_user():

    """Display a simple greeting."""
    print("Hello!")
#always leave a blank line between the end of the function and your next line of code.
greet_user()

print('\n--- Passing Information ---\n')

def greet_user(username):
    """Display a simpmle greeting."""
    print(f"Hello, {username.title()}!")

greet_user("Arnav")
greet_user("Arjun")

print('\n--- Arguments and Parameters ---\n')

name_1=input("What's your name? ")
def greet_user(username):
    """Display a simpmle greeting."""
    print(f"Hello, {username.title()}!")
greet_user(name_1)
