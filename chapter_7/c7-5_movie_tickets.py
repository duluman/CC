
"""
7-5. Movie Tickets: A movie theater charges different ticket prices depending on
a person’s age. If a person is under the age of 3, the ticket is free; if they are
between 3 and 12, the ticket is $10; and if they are over age 12, the ticket is $15.
Write a loop in which you ask users their age, and then tell them the cost of their
movie ticket.
"""

price = ['free', 10, 15]
exit_loop = ''
print("Hello, let me tel you how much is your ticket")
while exit_loop != 'quit':

    age = int(input("Tell me your age! "))
    if age < 3:
        print(f"For the age of {age} the ticket is {price[0]}")
    elif age < 12:
        print(f"You are {age} years old, you must pay {price[1]} $.")
    else:
        print(f"You are over {age} years old, you pay {price[2]} $.")

    print("If you want to quit the program, just type 'quit'.")