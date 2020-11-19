"""
7-2. Restaurant Seating: Write a program that asks the user how many people
are in their dinner group. If the answer is more than eight, print a message saying
they’ll have to wait for a table. Otherwise, report that their table is ready.
"""

group = input("How many people are in the dinner group?   ")

if int(group) < 8:
    print("The table is ready!")
else:
    print("Wait for a table please!")