"""
The modulo operator doesn’t tell you how many times
one number fits into another; it just tells you what the
remainder is.
"""


number = input("Enter a number, and I'll tell you if it's even or odd: ")
number = int(number)
if number % 2 == 0:
    print(f"\nThe number {number} is even.")
else:
    print(f"\nThe number {number} is odd.")