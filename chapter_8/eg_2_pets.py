"""
Because a function definition can have multiple parameters,
a function call may need multiple arguments. You can pass
arguments to your functions in a number of ways. You can
use positional arguments, which need to be in the same
order the parameters were written; keyword arguments,
where each argument consists of a variable name and a
value; and lists and dictionaries of values.
"""


def describe_pet(animal_type, pet_name):
    """Display information about a pet."""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")


describe_pet('hamster', 'harry')