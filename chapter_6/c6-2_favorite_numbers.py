"""
6-2. Favorite Numbers: Use a dictionary to store people’s favorite numbers.
Think of five names, and use them as keys in your dictionary. Think of a favorite
number for each person, and store each as a value in your dictionary. Print each
person’s name and their favorite number. For even more fun, poll a few friends
and get some actual data for your program.
"""

favorite_numbers = {
    'Cristian': 23,
    'Marius': 89,
    'Miky': 14,
    'Stefan': 27,
    'Tavi': 25
}

for name in favorite_numbers:
    print(f" -    {name} has {favorite_numbers[name]} as favorite number")