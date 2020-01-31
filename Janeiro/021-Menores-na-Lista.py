"""Exercício 21:
Usando List Comprehensions, retorne uma lista contendo todos os números menores do que X (parâmetro) em uma dada lista Y (parâmetro)"""


def menores_na_lista(referencia: int, lista: list):
    return list(set([numero for numero in lista if numero < referencia]))
