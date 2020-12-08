"""
Verificați dacă inputul de la user este “telacad”. În caz contrar cereți în mod repetat
reintroducerea – când inputul este cel dorit, afișați elementele acestei liste
[“telacad”, “peste 10 ani vechime”, “predare”,“cursuri oline”] într-un singur
string concatenat (cu spații între cuvinte).

"""


while not False:

    say_it = input("Va cer input  \n  \n ")
    lista_cu_elemente = ["telacad", "peste 10 ani vechime", "predare", "cursuri oline"]
    string_concatenat = ""
    if say_it == "telacad":
        for element in lista_cu_elemente:
            string_concatenat += element + " "
        print(string_concatenat)
        break
