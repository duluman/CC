
c = 5

while c:
    print(c)
    c -= 1

print("Final!")

c = 5

while c:
    if c == 3:
        print("Afisam pana ajungem la 3 >>> break")
        break
    print(c)
    c -= 1


c = 10

while c:
    if c % 2 == 0:
        print("Continue")
        c -= 1
        continue
    print("Afisam numerele impare", c)
    c -= 1

    if c == 0:
        print("Am ajuns la 0")
        break
