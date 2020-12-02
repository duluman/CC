
first_variable = "Telecom Academy preda cursuri de JavaScript"

print(first_variable.replace("JavaScript", "Python"))

# -------------------------------------------

"""
functia find()
verifica dacă un subșir de caractere face parte 
dintr-un șir de caractere mai mare, respectiv de pe ce poziție se găsește
"""
print(first_variable.find('preda'))
print(first_variable.find('Python'))  # returneaza -1 daca nu gaseste

# -------------------------------------------

secventa = ('telecom', 'academy', 'python')
desp = '+'
rezultat = desp.join(secventa)
print(rezultat)

