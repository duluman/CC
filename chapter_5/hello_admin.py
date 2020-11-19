"""
5-8. Hello Admin: Make a list of five or more usernames, including the name
'admin'. Imagine you are writing code that will print a greeting to each user after
they log in to a website. Loop through the list, and print a greeting to each user:
If the username is 'admin', print a special greeting, such as Hello admin,
would you like to see a status report?
Otherwise, print a generic greeting, such as Hello Jaden, thank you for
logging in again.
"""

users = ["Cristian", "Maria", "Stefan", "admin", "Larisa", "Valentin", "Lavinia"]

if users:
    for user in users:
        if user == "admin":
            print("\n Hello admin, would you like to see a status report? \n")
        else:
            print("Hello {}, thank you for logging in again.".format(user))
    print("\n \t \t Have a great day!")
else:
    print("The list must not be empty!")