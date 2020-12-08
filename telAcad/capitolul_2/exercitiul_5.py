"""
Citiți o valoare de la tastatură și efectuați următoarele
verificări -  dacă e mai mare ca 10 afișați
“numarul este mai mare ca 10”. Dacă este între 5 și 10 afișați
“numarul este intre 5 si 10” iar dacă este mai mic ca 5 afișați
“numarul este mai mic ca 5”.

"""
try:
    numar = int(input(" Tasteaza numarul, te rog! \n \n   "))
except:
    print("Nu ai tastat cifre!")
    numar = int(input("Hai, te rog, tasteaza cifre! \n"))

if numar > 10:
    print(" numarul este mai mare ca 10")
elif numar > 5:
    print(" numarul este intre 5 si 10 ")
else:
    print(" numarul este mai mic ca 5")

print("     T H E    E N D ")
