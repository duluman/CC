"""
Personal Message
Use a variable to represent a person’s name, and print
a message to that person. Your message should be simple, such as, “Hello Eric,
would you like to learn some Python today?”
"""

name = "Eric"

print(f'Hello {name}, would you like to learn some Python today?')
print("\n")
"""
Name Cases: Use a variable to represent a person’s name, and then print
that person’s name in lowercase, uppercase, and title case.
"""

variable_name = "Stefan"

print(variable_name.upper())
print(variable_name.lower())
print(variable_name.title())
print("\n")

"""
Find a quote from a famous person you admire. Print the
quote and the name of its author. Your output should look something like the
following, including the quotation marks:
Albert Einstein once said, “A person who never made a mistake never
tried anything new.”
"""

famous_person = "Les Brown"
print(f'{famous_person} once said: "You are never too old to set another goal or to dream a new dream"')
print("\n")
"""
Help others achieve their dreams and you will achieve yours.
Print the name once, so the whitespace around the name is displayed. Then
print the name using strip()
"""


famous_person = "       Les Brown   "
message = f'{famous_person} once said: "If you fall, fall on your back. If you can look up, you can get up."'
print(message)
print("\n")
message = f'{famous_person.strip()} once said: "Help others achieve their dreams and you will achieve yours."'
print(message)
