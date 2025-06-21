import formatting as f
import os

os.system("rm -r __pycache__")

f.title("Guided Practice #5")
f.dash()

print('--- Input Works ---\n')
message=input("Tell me something, and I will repeat it back to you:\t")
print(message)
print('\n--- Input Function ---\n')
color=input("What color is your nose? ")
print('Nose is', color)
name=input('Enter your Name: ')
print("Hello", name)
num=int(input('Enter a number: '))
add=num+1
print(add)
print('\n--- Multiple Prompts ---\n')
print('Please enter five grades. One at a time.')
grade1=input('Grade 1: ')
grade2=input('Grade 2: ')
grade3=input('Grade 3: ')
grade4=input('Grade 4: ')
grade5=input('Grade 5: ')
add=grade1+grade2+grade3+grade4+grade5
print(add)
print('\n--- Data Types ---\n')
sum_grades=int(grade1)+int(grade2)+int(grade3)+int(grade4)+int(grade5)
print(sum_grades)
print('\n--- The Average ---\n')
#average = sum / number of data points
average = sum_grades/5
print("The average is: "+str(average))
print("\n--- Print Formatting ---\n")
print('the average is: ', str(average))
print("\n--- Combining Functions ---\n")
message=input('Please type your Name: ').upper()
print(message)
print(message.title())
print(message.lower())
