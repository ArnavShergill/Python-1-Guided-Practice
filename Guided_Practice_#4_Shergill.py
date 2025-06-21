import formatting as f
import os

os.system("rm -r __pycache__")

f.title("Guided Practice #4")
f.dash()

print('--- Expression ---\n')
print(5==5)
print(5==6)
j='hel'
print(j+'lo'=='hello')
print('\n--- Comparison Operators ---\n')
x=5
y=3
result=x>y
print(result)#Output: True
result=x<y
print(result)#Output: False
result=x>=y
print(result)#Output: True
result=x<=y
print(result)#Output: False
result=x!=y
print(result)#Output: True
print('\n--- Logical Operators ---\n')
x=5
print(x>0 and x<10)
n=25
print(n%2==0 or n%3==0)
num1=5
num2=10
comparison1=num1<num2
result=not comparison1
print(result)
not (x and y)==(not x) or (not y)
not (x or y)==(not x) and (not y)
