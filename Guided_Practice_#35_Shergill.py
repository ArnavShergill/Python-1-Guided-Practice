from formatting import *

print("\n---- Guided Practice #35 ----\n")
section("Rounding Numbers")
subsection("Ceiling")

#importing the math library
import math

#round up
x = math.ceil(31.8)
print(x) #will print 32

short_dash()
subsection("Truncate")

#importing the math library
import math
x = math.trunc(31.8)
print(x) #will print 31

short_dash()
subsection("Floor")

#importing the math library
import math

#round down
x = math.floor(31.8)
print(x) #will print 31

short_dash()
subsection("Examples")

from math import floor, ceil, trunc

prize = 213

option1 = floor(213/2)

print("You get", option1, "and your friend gets", prize - option1)

from math import floor, ceil, trunc

prize = 213

option2 = ceil(213/2)
print("You get", option2, "and your friend gets",  prize - option2)

dash()
section("Generating Random Integers")
subsection("Random Integer Between A and B")

from random import randint
print(randint(1,10))

short_dash()
subsection("Randome Integer From a Range")

from random import randrange
print(randrange(1, 11))

from random import randrange
print(randrange(1, 11, 2))

short_dash()
subsection("Die Roller")

from random import randint

def die_roller():
    return (randint(1, 6))

# Role a die
print(die_roller())

short_dash()
subsection("Odd Random Integers")

from random import randrange

def odd_random():
    return (randrange(1, 102, 2))

#Generate an odd random integer
print(odd_random())

dash()
section("Random Sequences")
subsection("Selecting an Element From a List")

from random import choice

#Select Rock, Paper, or Scissors
def RPS():
    options=['Rock', 'Paper', 'Scissors']
    #return one of the elements at random
    return (choice(options))

#Generate an option
print(RPS())

short_dash()
subsection("Shuffling the Elements of a List")

from random import shuffle

x = ['Ana', 'John', 'Mike', 'Sally']

shuffle(x)

list_format(x)

short_dash()
subsection("Picking a Random Playing Card")

from random import choice

def pick_card():
    card_type = ['Clubs', 'Diamonds', 'Hearts', 'Spades']
    card_number = ['Ace', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'Jack', 'Queen', 'King']

    #Choose a type at random
    t = choice(card_type)
    n = choice(card_number)

    return[n, t]

#Show the randomly picked card
print(pick_card())

dash()

