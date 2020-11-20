"""
7-4. Pizza Toppings: Write a loop that prompts the user to enter a series of
pizza toppings until they enter a 'quit' value. As they enter each topping, print a
message saying you’ll add that topping to their pizza.
"""

statement = "What kind of topping do you want on your pizza? "
topping = ""
list_of_toppings = []
while topping != "quit":
    topping = input(statement)
    print(f"You just added '{topping}'")
    print("Type 'quit' if you want to stop!")
    list_of_toppings.append(topping)

print(f"Your toppings are: \n {list_of_toppings}")