
"""
x = numarul vostru la începutul programului. Dacă este integer adunați 3,
dacă este float împarțiti-l pe x la 2 iar dacă este imaginar extrageți partea reală,
partea imaginară și calculați modulul. Afișati rezultatul pentru fiecare operație.
(folosiți “isinstance()” pentru această comparație)
"""


# x = 3
# x = 3.0
x = 2 + 3j

if isinstance(x, int):
    print(x + 3)
elif isinstance(x, float):
    print(x / 2)
elif isinstance(x, complex):
    print("partea reala = ", str(x.real))
    print("partea imaginara = ", str(x.imag))
