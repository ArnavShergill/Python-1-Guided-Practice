import formatting as f
import os

os.system("rm -r __pycache__")

f.title("Guided Practice #2")
f.dash()

print('--- Variables ---\n')
score=0
print(score)
score=score+1
print(score)
score+=1
print(score)
message='This is a string of data'
print(message)
print('\n--- Methods ---\n')
name="ada lovelace"
print(name.title())
print(name.upper())
print(name.lower())
print('\n--- String Addition ---\n')
message1='This is for a grade. '
message2='No seriously, it is, I promise.'
message3=message1+message2
print(message3)
#I think that it will add message 1 with message 2 as if it both were written within one print command.
print('\n--- Reassignment ---\n')
num1=6
print(num1)
num1=8
print(num1)
#I think it is going to print 6 first and then it will print 8 afterwards.
print('\n--- Print Variables ---\n')
message='Hopefully this is easy'
message1='What is your name?'
print(message)
print(message1+" "+'Arnav S.')
print('\n--- Variables in Strings ---\n')
print('--- Full Name ---')
first_name="ada"
last_name="lovelace"
full_name=f"{first_name} {last_name}"
print(full_name.title())
message=f"Hello, {full_name.title()}"
print(message+'.')
