"""
A dictionary in Python is a collection of key-value pairs.
Each key is connected to a value, and you can use a key to
access the value associated with that key. A key’s value can
be a number, a string, a list, or even another dictionary. In
fact, you can use any object that you can create in Python as
a value in a dictionary.
In Python, a dictionary is wrapped in braces, {}, with a
series of key-value pairs inside the braces
"""

alien_0 = {'color': 'green', 'points': 5}
print(alien_0)
alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0)
alien_0['speed'] = 'medium'
print(alien_0)

"""
You can loop through all of a dictionary’s key-value pairs, through its keys, or through its values.
"""

text = "You can loop through all of a dictionary’s key-value pairs, through its keys, or through its values."
print(len(text))

user_0 = {
    'username': 'efermi',
    'first': 'enrico',
    'last': 'fermi',
}
for key, value in user_0.items():  # loop through the dictionary using a for loop
    print(f"\nKey: {key}")
    print(f"Value: {value}")
print("\n", " - " * 7, "\n")

favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}
print("Favorite languages:")
for name in favorite_languages.keys():
    print("   Hello friends, my name is:")
    print(f"{name.title()} and I like to stydy '{favorite_languages[name]}'\n")

print("\n", " - " * 7, "\n")

print("Favorite languages sorted by name:")
for name in sorted(favorite_languages.keys()):
    print("   Hello friends, my name is:")
    print(f"{name.title()} and I like to stydy '{favorite_languages[name]}'\n")