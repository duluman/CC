"""
Checking Usernames: Do the following to create a program that simulates
how websites ensure that everyone has a unique username.
Make a list of five or more usernames called current_users.
Make another list of five usernames called new_users. Make sure one or two
of the new usernames are also in the current_users list.
Loop through the new_users list to see if each new username has already been
used. If it has, print a message that the person will need to enter a new
username. If a username has not been used, print a message saying that the
username is available.
Make sure your comparison is case insensitive. If 'John' has been used,
'JOHN' should not be accepted. (To do this, you’ll need to make a copy of
current_users containing the lowercase versions of all existing users.)
"""

current_users = ["chris", "jhon", "SangReal", "PyAdmin", "Atlantis", "ryzen"]
list_current = []
for user in current_users:
    list_current.append(user.lower())


new_users = ["Adata", "Chris", "Wick", "Cash", "Ryzen"]
list_new = []
for user in new_users:
    list_new.append(user.lower())

for user in list_new:
    if user in list_current:
        print(f"The username '{user}' is taked")

        another_user = input("Try another username: ")
        list_current.append(another_user)
        # list_current(user) = another_user
    else:
        list_current.append(user)
print("The users are:")
for element in list_current:
    print("  - ", element.title())
