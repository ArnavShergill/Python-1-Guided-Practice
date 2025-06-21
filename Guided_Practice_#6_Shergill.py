import formatting as f
import os

os.system("rm -r __pycache__")

f.title("Guided Practice #6")
f.dash()

print('--- The Modulo Operator ---\n')
number=input("Enter a number, and I'll tell you if it's even or odd: ")
number = int(number)
if number % 2 == 0:
    print(f"\nThe number {number} is even.")
else:
    print(f"\nThe number {number} is odd")
print("\n--- Float & Int ---\n")
#Conversion from float to int
num=9.3
#printing data type of "num"
print('type:',
      type(num).__name__)
#conversion to int
num=int(num)
#printing data type of 'num'
print('converted value:', num,
      ',type:', type(num).__name__)
print()
#example of unpredictable
#behavior of int()
num1=5.9
num2=5.9999999999999999999999999999999999999999999999999999
num1=int(num1)
num2=int(num2)
print(num1, num2, sep='\n')
print('\n--- Operands ---\n')
print(2+3)
print(2-3)
print(2*3)
print(2**3)
print(3**2)
print()
minutes=645
hours=minutes//60
print(hours)
print()
quotient=7//3 #This is the integer division operator
print(quotient)
remainder = 7%3
print(remainder)
print()
total_secs=7684
hours=total_secs//3600
print(hours)
secs_still_remaining=total_secs%3600
print(secs_still_remaining)
minutes=secs_still_remaining//60
print(minutes)
secs_finally_remaining=secs_still_remaining%60
print(secs_finally_remaining)
