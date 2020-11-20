
"""
You can use a while loop to count up through a series of numbers.
"""
current_number = 1

while current_number <= 7:
    print(current_number)
    current_number += 1

prompt = "\nTell me something, and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program. "
message = ""
parrot = 0
while message != 'quit':
    message = input(prompt)
    print(message)
    parrot += 1
    print(f"Purrfect for the {parrot} time!")