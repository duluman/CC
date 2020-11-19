"""
All indented lines after an if statement will be
executed if the test passes, and the entire block of indented
lines will be ignored if the test does not pass.
"""

age = 16

if age >= 18:
    print(f"You are {age} old. You are old enough to vote!")
else:
    print(f"You have {18-age} years to wait until you can vote!")
    print("Sorry, you are too young to vote.")
