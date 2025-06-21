print('---- Guided Practice #4 ----\n')

import time

def section(section_name):
    print(f'--- {section_name} ---\n')

def dash():
    print('\n--------------------------------------\n')

def wait_time(seconds=3):
    time.sleep(seconds)

section('Looping Through an Entire List')

magicians=['alice','david','carolina']
for magician in magicians:
    print(magician)
dash()
wait_time()

section('A Closer Look at Looping')
dash()
wait_time()
section('Doing More Work Within a FOR Loop')

magicians=['alice','david','carolina']
for magician in magicians:
    print(f'{magician.title()}, that was a great trick!')
    print(f'I can\'t wait to see your next trick, {magician.title()}.\n')
dash()
