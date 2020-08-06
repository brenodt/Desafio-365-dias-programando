"""Exercício 42:
Fischer-Yates Shuffle

Dada uma lista A de tamanho n, embaralhe seus elementos de maneira aleatória.

Algoritmo para reorganizar a lista:

for i from n-1 downto 1 do
    j = random integer such that 0 <= j <= i
    exchange A[j] and A[i]
"""

from math import floor
from random import uniform

def fischer_yates(lista: list):
    i = len(lista) - 1
    while i >= 0:
        j = floor(uniform(0, i))
        pivo = lista[j]
        lista[j] = lista[i]
        lista[i] = pivo
        i -= 1
    return lista

t = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
y = fischer_yates(t)
print(y)
