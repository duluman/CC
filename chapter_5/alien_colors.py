import random
"""
5-3. Alien Colors #1: Imagine an alien was just shot down in a game. Create a
variable called alien_color and assign it a value of 'green', 'yellow', or 'red'.
Write an if statement to test whether the alien’s color is green. If it is, print a
message that the player just earned 5 points.
"""

color = ["green", "yellow", "red"]

alien_color = random.choice(color)

print(alien_color)

if alien_color == "green":
    print("Alien color is {}".format(alien_color))
    print("You just earn 5 points")

print('\n')

"""
5-4. Alien Colors #2: Choose a color for an alien as you did in Exercise 5-3, and
write an if-else chain.
If the alien’s color is green, print a statement that the player just earned 5
points for shooting the alien.
If the alien’s color isn’t green, print a statement that the player just earned 10
points.
"""
if alien_color == "green":
    print("Alien color is {}".format(alien_color))
    print("You just earn 5 points")
elif alien_color == "red":
    print("You earn 10 points for the red color of the alien")
else:
    print("Wow ...15 points for the yellow color of the alien")

