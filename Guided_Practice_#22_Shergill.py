print('---- Guided Practice #22 ----\n')

def section(section_name):
    print(f'--- {section_name} ---\n')

def dash():
    print('\n----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------\n')

def short_dash():
    print('-----------------------\n')

section("Moving From One List to Another")

#Start with users that need to be verified,
# and empty list to hold confirmed users.

unconfirmed_users = ['alice', 'brian', 'candace']
confirmed_users = []

# verify each user until there are no more unconfirmed users,
# move each verivied user into the list of confirmed users.

while unconfirmed_users:
    current_user = unconfirmed_users.pop()
    print(f'Verifying user: {current_user.title()}')
    confirmed_users.append(current_user)

# Display all confirmed users.
print('\nthe following users have been confirmed: ')
for confirmed_user in confirmed_users:
    print(confirmed_user.title())

dash()
section('Removing All Instances from a List')

pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']
print(pets)

while 'cat' in pets:
    pets.remove('cat')

print(pets)
dash()
section('Copy() Method')

#Original List
grades = [84, 90, 78, 92]

#Create a copy
grades_copy = grades.copy()

#Sort the copy
grades_copy.sort()

print("Original Grades:", grades)
print("Sorted Grades:", grades_copy)
