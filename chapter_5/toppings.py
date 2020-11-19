

requested_toppings = ['mushrooms', 'green peppers', 'extra cheese']
print("Star making your pizza:")
for requested_topping in requested_toppings:
    print(f" - Adding {requested_topping}.")

print("\nFinished making your pizza! \n")

"""
People will ask for just about anything, especially when it
comes to pizza toppings. What if a customer actually wants
french fries on their pizza?
"""

available_toppings = ['mushrooms', 'olives', 'green peppers', 'pepperoni', 'pineapple', 'extra cheese']
requested_toppings = ['mushrooms', 'french fries', 'extra cheese']
for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
        print(f" + Adding {requested_topping}.")
    else:
        print(f" - Sorry, we don't have {requested_topping}.")
print("\nFinished making your pizza!")