"""Exercício 49:

Receba uma string e o índice a ser eliminado. Retorne a string corrigida.
"""


def remove_i(texto:str, i: int):
    return texto[:i] + texto [i + 1:]


t = "Breno"
ind = 3
print(remove_i(t, ind))
