import formatting as f
import os

os.system("rm -r __pycache__")

f.title("Guided Practice #14")
f.dash()

f.section('Using List/Array Slicing Method')

#Python program to demonstrate string slicing

#String Slicing
string='ASTRING'

#Using slice constructor
s1=slice(3)#display everything before index 3
s2=slice(1,5,2)#start at index 1, go to index 5, count every 2
s3=slice(-1,-12,-2)#start at index -1, go to index -12, county every -2

print(string[s1])
print(string[s2])
print(string[s3])

f.dash()

#List/Array Slicing

string = 'COXMILLCHARGERS'

#Using indexing sequence
print(string[:7])

f.dash()

#List/Array Slicing

string = 'COXMILLCHARGERS'

#Using indexing sequence
print(string[:7])
print(string[1:5:2])

f.dash()

#List/Array Slicing

string = 'COXMILLCHARGERS'

#Using indexing sequence
print(string[:7])
print(string[1:5:2])
print(string[-1:-12:-2])

f.dash()

#List/Array Slicing

string = 'COXMILLCHARGERS'

#Using indexing sequence
print(string[:7])
print(string[1:5:2])
print(string[-1:-12:-2])
print(string[::-1])

f.section('String Methods')
f.section('Len() Method')

my_string='Hello, World!'
print(len(my_string)) #Output: 13

f.section('Count() Method')

my_string="Hello, world! Hello Everyone!"
def my_string_count(String_Count):
    print(my_string.count(String_Count))

my_string_count('Hello')#Output: 2
my_string_count('e')#Output: 5
print(my_string.count('I', 0, 5))#Output: 2, counts 'I' within the first 'Hello'

f.section('Find() Method')

print(my_string.find('world'))#Output: 7
print(my_string.find('z'))#Output: -1 since 'z' is not in the string
print(my_string.find('o', 5, 10))#Output 8, searches for 'o' between indices 5  and 10

f.section('Combining Them')

#Ask the user for input
sentence=input('Enter a sentence: ')
word=input('Enter a word to find: ')

#Use .find() to check if the word exists
if sentence.find(word)!=-1:
    print(f"'{word}' was found in the sentence.")
    #Use .count() to count occurrences
    occurrences = sentence.count(word)
    print(f"Number of occurrences of '{word}': {occurrences}")
else:
    print(f"'{word}' was not found in the sentence.")

f.section('With Loops')

sentence = "Learning Python programming is fun and offers a great way to solve problems."

words_to_find=['Python', 'fun', 'solve']

for word in words_to_find:
    if sentence.find(word) != -1:
        print(f"Found '{word}' in the sentence.")
    else:
        print(f"'{word}' was not found in the sentence")
