"""Exercício 44:
Simule um Jogo de cara ou coroa,
o usuário determina quantas vezes a moeda será jogada.

Retorne o número de vezes que cada lado caiu.
"""


from random import choice

def cara_coroa(vezes: int):
    vez = 0
    resultado = {"cara": 0, "coroa": 0}
    while vez < vezes:
        escolha = choice(["cara", "coroa"])
        resultado[escolha] += 1 
        vez += 1

    return resultado


repete = 5
print(cara_coroa(repete))
