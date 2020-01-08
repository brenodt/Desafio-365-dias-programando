"""Exercício 7:
Dadas duas listas, retorne uma nova lista contendo valores que aparecem nas duas da entrada"""


def repetidos_versao_1(lista1: list, lista2: list):
    saida = list(set([x for x in lista1 for y in lista2 if x == y]))

    return saida


def repetidos_versao_2(lista1: list, lista2: list):
    auxiliar = [x for x in lista1 for y in lista2 if x == y]
    saida = []
    for item in auxiliar:
        if item not in saida:
            saida.append(item)

    return saida


a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
print(repetidos_versao_1(a, b))
print(repetidos_versao_2(a, b))
