"""
Captați de la utilizator input, convertiți-l în integer și verificați dacă e mai mare ca 2.
Dacă nu, cereți alt input până este introdusă o valoare mai mare decât 2, apoi calculați
suma de la 1 până la valoarea introdusă de utilizator: 1+2+...+n.

"""

while "Adavarat":
    numar = int(input("Spune-mi un numar: \n \t ...  "))

    if numar < 2:
        continue
    suma = 0
    for pas in range(1, numar+1):
        suma += pas
    if suma > 0:
        print("Pentru numarul {}, suma este: {}".format(numar, suma))
        break

