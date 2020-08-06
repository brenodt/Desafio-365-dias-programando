"""
Exercício 50:

"""

def remova_elementos(lista: list, elementos: tuple):
    return [elemento for elemento in lista if elemento not in elementos]


listas = [11, 5, 17, 18, 23, 50]
x = (5, 18)

print(remova_elementos(listas, x))
