import getpass
response = input("Please enter your name: ")

print("Thank you, ", response)

print("Numele tau are ", response.__len__(), "caractere")

password = getpass.getpass("Va rog sa tastati parola: ")

print("I can see your password", response, "\n Is it ... \'", password, "\'?")

