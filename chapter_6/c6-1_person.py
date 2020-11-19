"""
6-1. Person: Use a dictionary to store information about a person you know.
Store their first name, last name, age, and the city in which they live. You should
have keys such as first_name, last_name, age, and city. Print each piece of
information stored in your dictionary.
"""

person = {
    'first_name': "Cristian",
    'last_name': "Duluman",
    'age': 31,
    'city': "Craiova"
}

print("I will show you what I stored in my personal dictionare: \n")
print(f" - First name is {person['first_name']}")
print(f" - Last name is: {person['last_name']}")
print(f" - Age: {person.get('age', 'confidential')}")
print(f" - City: {person.get('city', 'Confidential')}")
print(f" - Job title: {person.get('job', 'Confidential')}")