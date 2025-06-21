import time
import formatting as f

print("\n---- Guided Practice #33 ----\n")
f.section("Importing an Entire Module")

import Pizza

Pizza.make_pizza(16, 'pepperoni')
Pizza.make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')

f.dash()
f.section("Importing Specific Functions")

from Pizza import make_pizza

make_pizza(16, 'sausage')
make_pizza(12, 'Onions', 'Green Peppers', 'bacon')

f.dash()
f.section("Using as to Give a Function on Alias")

from Pizza import make_pizza as mp

mp(9, 'sardines')
mp(12, 'chicken', 'bacon', 'ranch')

f.dash()
f.section("Using as to give a Module an Alias")

import Pizza as p

p.make_pizza(16, 'pineapple')
p.make_pizza(12, 'pineapple', 'ham', 'bacon', 'bbq sauce')

f.dash()
f.section("Importing All Functions in a Module")
from Pizza import *

make_pizza(16, 'jalapenos')
make_pizza(12, 'spinach', 'red onion', 'pepperoni', 'bacon', 'lamb sausage')

f.dash()
