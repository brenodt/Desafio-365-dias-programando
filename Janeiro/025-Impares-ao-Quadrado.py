"""Exercicio 25:
Use List Comprehension para elevar ao quadrado todos os números ímpares de uma lista.
"""


def impares_ao_quadrado(lista: list):
    return [numero ** 2 for numero in lista if numero % 2 != 0]


a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(impares_ao_quadrado(a))
