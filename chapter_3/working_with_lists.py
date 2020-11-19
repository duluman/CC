bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles)
"""
To access an element in a list, write the name of the
list followed by the index of the item enclosed in square
brackets.
"""
print(bicycles[0])  # Index Positions Start at 0

print(bicycles[-1])  # Python has a special syntax for accessing the last element in a list.


message = f'My first bicycle was {bicycles[1].title()}'
print(message)

"""
3-1. Names: Store the names of a few of your friends in a list called names. Print
each person’s name by accessing each element in the list, one at a time.
"""

names = ['Marius', 'Tavi', 'Ionut', 'Andrei']
print("My friends are:")
for i in range(len(names)):
    print(" -  ", names[i], "v1")

print("My friends are:")
for element in names:
    print(" -- ", element, "v2")

"""
3-2. Greetings: Start with the list you used in Exercise 3-1, but instead of just
printing each person’s name, print a message to them. The text of each message
should be the same, but each message should be personalized with the person’s
name.
"""
print(f'Good to see you, {names[0]}')
print(f'Hello, {names[1]}')
print(f"Long time, no see {names[2]}")
print(f'Hello my friend, {names[3]}')


motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
motorcycles[0] = 'ducati'  # change the value of this first item
print(motorcycles)

motorcycles.append('honda')  # adds to the end of the list without affecting any of the other elements in the list
print(motorcycles)

motorcycles.insert(0, 'bmw') # This operation shifts every other value in the list one position to the right

print(motorcycles)

del motorcycles[-1]
print (motorcycles)


"""
Removing an Item Using the pop() Method
Sometimes you’ll want to use the value of an item after you
remove it from a list. In a web
application, you might want to remove a user from a list of
active members and then add that user to a list of inactive
members.
The pop() method removes the last item in a list, but it lets
you work with that item after removing it.
"""

popped_motorcycle = motorcycles.pop()
print(motorcycles)
print(popped_motorcycle)

"""
Sometimes you won’t know the position of the value you
want to remove from a list. If you only know the value of
the item you want to remove, you can use the remove()
method.
"""
motorcycles.remove('ducati')
print(motorcycles)
