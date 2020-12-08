"""
Verificați dacă un număr introdus de utilizator este par sau impar.
"""

numar = int(input(" Spune-mi un numar si eu iti voi afisa daca este par sau impar ^ _ ^ \n ... \t"))

if numar % 2 == 0:
    print(f"numarul {numar} este par")
else:
    print("numarul {} este impar".format(numar))
