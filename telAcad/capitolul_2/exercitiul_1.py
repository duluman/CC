"""
Folosind WHILE citiți input de la tastatură până când acesta este egal cu ”telacad”.
În momentul în care această condiție este îndeplinită, ieșiți din buclă și apoi
afișați mesajul “Sfarsitul programului”.

"""


while True:
    citire = input("Infinit: ")
    if citire == "telacad":
        break

print("Sfarsitul programului")