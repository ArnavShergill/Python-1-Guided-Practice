import formatting as f
import os

os.system("rm -r __pycache__")

f.title("Guided Practice #1")
f.dash()

f.slow_print('---print Function---')
print()
f.slow_print("This is some text to output to the user using the print function.")
print()
f.slow_print('--- Strings ---')
print()
f.slow_print('He said to the class "Sometimes you need to shutdown and restart your Chromebook to get it to connect to the internet" ')
f.slow_print("It's time to save your code.")
print()
f.slow_print("---Triple Quotes ---")
print()
"""This is a really long comment that can make the code ugly and uncomfortable to read on a small screen so it needs to be broken into multiline strings using double tripple quotes"""
'''This is a really long comment that can make the code ugly and uncomfortable to read on a small screen so it needs to be broken into multiline strings using double tripple quotes'''
print()
f.slow_print('--- String Creation---')
print()
f.slow_print("""This is a really long comment that can make the code ugly and uncomfortable to read on a small screen so it needs to be broken into multiline strings using double tripple quotes""")
f.slow_print("""This is a really long comment that can
make the code ugly and uncomfortable to read
on a small screen so it needs to be broken into
multiline strings using double tripple quotes""")
print()
text_variable='''This is a really long comment that
can make the code ugly and uncomfortable to read
on a small screen so it needs to be broken into multiline
strings using double tripple quotes'''
f.slow_print(text_variable)
print()
f.slow_print('--- Comments ---')
print()
#This is my first Python Program, "Hello World!"
f.slow_print('Teacher says: Hello World!')
print()
#This is totally ligit
message = 'One of Python\'s strengths\n is its diverse \tcommunity'
f.slow_print(message)
print()
f.slow_print('--- Escape Sequence Example ---')
f.slow_print("\n--- Backslash ---\n")
f.slow_print("This is a backslash: \\")
f.slow_print("\n--- Single Quote ---\n")
f.slow_print("I\'m learning Python\'s escape sequences!")
f.slow_print("\n--- Double Quote ---\n")
f.slow_print("she said, \"Hello!\"")
f.slow_print("\n--- New Line ---\n")
f.slow_print("Hello\nWorld")
f.slow_print("\n--- Tab ---\n")
f.slow_print("Name:\tJohn")
