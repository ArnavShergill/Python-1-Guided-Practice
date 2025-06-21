from formatting import *
from datetime import *

print("\n---- Guided Practice #37 ----\n")
section("Creating timedelta Objects")
subsection("Explicit Definition")

delta1 = timedelta(days = 7, hours = 2)
print(delta1)

short_dash()
subsection("Calculating Difference Between Two datetime Objects")

dt1 = datetime(year = 2017, month = 1, day = 1)
dt2 = datetime(year = 2017, month = 2, day = 1)
delta2 = dt2 - dt1
print(delta2)

short_dash()
subsection("Getting the timedelta Attributes")

print(delta1.days)

print(delta1.seconds)

print(delta1.microseconds)

short_dash()
subsection("Total Number of Seconds")

print(delta1.total_seconds())

dash()
section("Performing Date Arithmatic")
subsection("Arithmetic using datetime and timedelta Objects")

#Define a timedelta object
one_hundred_days = timedelta(days = 100)

#Get today's date
current_date = datetime.today()

#Compute the new date
new_date = current_date + one_hundred_days

#Print formatted date
print("After 100 days:", new_date.strftime("%b/%d/%Y"))

short_dash()
subsection("Finding the Dates 200 and 300 days from Today")

#Define the timedelta objects
one_hundred_days = timedelta(days = 100)
two_hundred_days = one_hundred_days * 2
three_hundred_days = one_hundred_days * 3

# Get today's date
current_date = datetime.today()

#Compute the new dates
new_date1 = current_date + two_hundred_days
new_date2 = current_date + three_hundred_days

#Print formatted new dates
print("After 200 days:", new_date1.strftime("%b/%d/%Y"))
print("After 300 days:", new_date2.strftime("%b/%d/%Y"))

dash()
section("Comparing datetime Objects")

#Birthday of person 1
birthday1 = date(year = 1993, month = 3, day = 5)

#Birthday of person 2
birthday2 = date(year = 2003, month = 3, day = 20)

#Compare birthdays
if (birthday1 > birthday2):
    print("Person 2 is older")
elif (birthday1 < birthday2):
    print("Person 1 is older")
else:
    print("Person 1 and Person 2 are of the same age")

dash()
section("Creating Useful Applications")

#Define today's date
now = datetime.today()

#December solstice of year 1, it can be any year, it will be changed later
solstice = datetime(month= 12, day = 21, year = 1)

#Change solstice's year to current year
solstice = solstice.replace(year = (datetime.today().year))

#Get the timedelta
count = solstice = now

#Display the solstice countdown
print("Therer are", count.day, "days until the December solstice!")

dash()
