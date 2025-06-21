print('\n---- Guided Practice #25 ----\n')

import time

def section(section_name):
    print(f'--- {section_name} ---\n')

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

section('Defining a Tuple')

dimensions = (200, 50)
print(dimensions[0])
print(dimensions[1])

short_dash()

#If we try this what happens?

dimensions = (200, 50)

try:
    dimensions[0]=250
except TypeError:
    print('Error: Object does not support item assignment.')

short_dash()

my_t=(3,)
print(type(my_t))

dash()
section('Looping Through All Values in a Tuple')

dimensions = (200,50)
for dimensions in dimensions:
    print(dimensions)

dash()
section('Writing Over a Tuple')

dimensions=(200, 50)
print("Original dimensions:\n")
for dimension in dimensions:
    print(dimension)

short_dash()

dimensions= (400, 100)
print("Modified dimensions:\n")
for dimension in dimensions:
    print(dimension)
dash()
section('Can/Can\'t')

#Tuple of popular social media platforms
social_media_tuple=("Instagram","TikTok", "Snapchat", "Twitter")

#Attempting to modify the tuple
try:
    social_media_tuple[2] = "YouTube"
except TypeError as e:
    print("Oops! Tuples are immutable. Error:", e)

#The tuple remains unchanged
    print(social_media_tuple)

short_dash()

tuple1=(1,2,3,2,1)
print("The number two appears:", tuple1.count(2), "times")
print("the number 3 appears at index", tuple1.index(3))

short_dash()

#Tuple of popular social media platforms
social_media_tuple=("Instagram","TikTok", "Snapchat", "Twitter")

#Converting the tuple to a list
social_media_list=list(social_media_tuple)

#Adding a new platform to the list
social_media_list.append("Discord")

#Adding a new platform to the list
social_media_tuple = tuple = tuple(social_media_list)

#Printing the updated tuple
print(social_media_tuple)

dash()
