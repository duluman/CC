import getpass
academy = input("What is your academy? \n \t")
language = input("What language are you learning? \n \t")
print("Your Academy is " + academy + " and you are learning " + language)

username = input("What is your username? \n \t")
password = getpass.getpass("What is your password ? \n \t")

print("Your username is: " + username)
print("Your password is: " + password)