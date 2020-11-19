favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}

language = favorite_languages['jen'].title()
print(f'Sarah s favorite language is {language}')

"""
The get() method requires a key as a first argument. As a
second optional argument, you can pass the value to be
returned if the key doesn’t exist:
"""

get_language = favorite_languages.get('chris', 'We dont know Chris')
print(get_language)

"""
If the key 'points' exists in the dictionary, you’ll get the
corresponding value. If it doesn’t, you get the default value.
"""