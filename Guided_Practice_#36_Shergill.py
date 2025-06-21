from formatting import *

print("\n---- Guided Practice #36 ----\n")
section("localtime()")

#Get the current timestamp
current_time = time.time()

#Convert the timestamp to local time struct
local_time=time.localtime(current_time)

#Extract individual components from the local time struct
year = local_time.tm_year
month = local_time.tm_mon
day = local_time.tm_mday
hour = local_time.tm_hour
minute=local_time.tm_min
second=local_time.tm_sec

#Print the local time components
print(f"Current local time: {year}-{month}-{day} {hour}:{minute}:{second}")

dash()
section("Time Objects")
subsection("Assigning a Time Object")

print("In order:")
from datetime import time

#Time is 8:55:20.000500 PM (or 0:55:20.000500)
t = time(20, 55, 20, 500)
print(f"\n{t}\n")

print("by name")

t=time(minute=10, hour = 9, microsecond = 900000, second = 20)
print(f"\n{t}")

short_dash()
subsection("Getting Time object attributes (Hour, minute... etc.)")

print("Some Attributes:\n")

#Time is 1:10 (or 13:10:00:000000)
t=time(hour = 1, minute = 10)
print(t)

print("\nGetting an Attribute:\n")

#assign a time variable t
t = time(hour = 9, minute = 10, second = 43, microsecond = 100)

#access each of the attributes separately
h = t.hour # will be 9
m = t.minute # will be 10
s = t.second # will be 43
ms = t.microsecond # will be 100

print(f"The time is: {h} hours {m} minutes {s} seconds and {ms} microseconds.")

short_dash()
subsection("Modifying Time object attributes (Hour, minute... etc.)")

#assign t as 9:10:43:0000100
t = time(hour = 9, minute = 10, second = 43, microsecond = 100)
print("Old time: ", t)

#modify hour and minute
t = t.replace(hour = 8, minute = 8)
print("New time: ", t)

dash()
section("Date Objects")

from datetime import date

#Using al attributes in order (year, month, day) without names
# date1 is May 7 2013
date1 = date(2013, 5, 7)
print("Date1 is: ", date1)

#using all attributes with names and not necessarily in order
#date2 is April 23 1999
date2 = date(day = 23, month = 4, year = 1999)
print("date2 is: ", date2)

print("\nDate Attribute:\n")

#assign a date variable
SpecialDate = date(year = 2017, month = 11, day = 15)

y = SpecialDate.year #will be 2017
m = SpecialDate.month #will be 11
d = SpecialDate.day # wil be 15

print("The Special date is: / Month: ", m, "/ Day: ", d, "/ Year: ", y)

print("\nModifying Date Object:\n")

#assign a date
SomeDate = date(year = 2015, day = 28, month = 2)
print("Old date: ", SomeDate)

#modify year and day
#2016 is a leap year, so we can set the date to Feb 29 2016
SomeDate = SomeDate.replace(year = 2016, day = 29)
print("New date: ", SomeDate)

short_dash()
subsection("Current Local Date")

#get today's date
d= date.today()
print(d)

dash()
section("Datetime Objects")
subsection("Setting a DateTime Object to the Current Local Date & Time")

print("\nAssign datetime:\n")

from datetime import datetime

#July 4, 2022, at 4:30 PM

#Method 1
dt = datetime(2022, 7, 4, 16, 30)
print("Method 1: ", dt)

#Method 2
dt = datetime(day = 4, month = 7, year = 2022, minute = 30, hour = 16)
print("Method 2: ", dt)

print("\nGetting datetime:\n")

# July 4th 2022, at 4:30 PM
dt = datetime(2022, 7, 4, 16, 30)

#access year
print("Year is: ", dt.year)

#access minute
print("Minute is: ", dt.minute)

print("\nModifying datetime:\n")

# July 4th 2022, at 4:30 PM
dt = datetime(2022, 7, 4, 16, 30)

#change year to 2020 and second to 30
dt = dt.replace(year = 2020, second = 30)
print(dt)

print("\nCurrent datetime:\n")

#get today's date and current local time
dt = datetime. today()
print(dt)

short_dash()
subsection("Splitting a datetime Object into Separate date and time Objects")

print("Splitting datetime:\n")

from datetime import datetime, time, date

#get today's date and current local time
dt = datetime.today()

#split tino time t and date d
t = dt.time()
print("Time is: ", t)

d = dt.date()
print("Date is: ", d)

short_dash()
subsection("Combining Separate date and time Objects into a Single datetime Object")

print("Combining datetime\n")

#assign a time object
t= time(hour = 6, minute = 45, second = 0)

#assign a date object
d = date.today()

#combine t and d into a datetime object
dt = datetime.combine(date = d, time = t)

print(dt)

dash()
section("Date/Time Examples")
subsection("Formatting time Objects")

t = time(hour = 10, minute = 15)

#display as 10:15 AM
#string passed to strftim includes all necessary spaces and semicolons
formatted_string = t.strftime("%I:%M %p")
print("First format: ", formatted_string)

#display as 10:15:00 (24 hour clock, no AM/PM)
formatted_string = t.strftime("%H:%M:%S")
print("Second format: ", formatted_string)

short_dash()
subsection("Formatting date Objects")

d = date(year = 1999, month = 11, day = 3)

#display as November, 03, 1999
#string passed to strftime includes all necessary spaces and commas
formatte_string = d.strftime ("%B, %d, %Y")
print("First format: ", formatted_string)

#display as Nov 03 99
formatted_string = d.strftime("%b %d %y")
print("Second format: ", formatted_string)

dash()
section("Formatting datetime Objects")

dt = datetime(year = 1999, month = 11, day = 3, hour = 10, minute = 15)

#display as November, 03, 1999, @ 10:15 AM
formatted_string = dt.strftime("%B, %d, %Y @ %I:%M %p")
print("First format: ", formatted_string)

#display as Nov 03 99 / 10:15:00
formatted_string = dt.strftime("%b %d %y / %H:%M:%S")
print("Second format: ", formatted_string)

dash()
