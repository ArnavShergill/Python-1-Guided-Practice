import formatting as f
import os

os.system("rm -r __pycache__")

f.title("Guided Practice #9")
f.dash()

print('\n--- Return Values ---\n')

def get_formatted_name(first_name, last_name):
    """Return a full name, neatly formatted."""
    full_name=f"{first_name} {last_name}" #Local Variable
    return full_name.title()

musician=get_formatted_name("jimi","hendrix") #Global Variable
print(musician)

print('\n--- Optional Argument ---\n')

def get_formatted_name(first_name, last_name, middle_name=''):
    """Return a full name, neatly formatted."""
    if middle_name:
        full_name=f"{first_name} {middle_name} {last_name}" #Local Variable
    else:
        full_name=f'{first_name} {last_name}'#Local Variable
    return full_name.title()

musician=get_formatted_name("jimi","hendrix") #Global Variable
print(musician)

musican=get_formatted_name('olivia','newton','john') #Global Variable
print(musican)

