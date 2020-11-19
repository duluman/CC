

for value in range(1, 5):
    print(value)

numbers = list(range(1, 6))
print(numbers)

even_numbers = list(range(2, 22, 2))
print(even_numbers)

digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]

print(min(digits))
print(max(digits))
print(sum(digits))


"""
A list comprehension combines the for
loop and the creation of new elements into one line, and
automatically appends each new element.
"""
squares = [value**2 for value in range(1, 11)]
print(squares)

plus_2 = [value+2 for value in range(20)]
print(plus_2)

cube = [value**3 for value in range(3, 30)]
print(cube)