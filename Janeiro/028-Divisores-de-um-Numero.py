"""Exercicio 28:
Dado um número N, determine quais são os divisores deste número.

Divisores são aqueles que dividem um dado número em partes iguais (sem resto).
"""


def divisores(numero: int):
    # inicializo a lista de divisores
    divisores = []
    # para cada numero no range...
    # Como o segundo parâmetro de
    # range() não é incluso, adiciono 1
    for divisor in range(2, numero + 1):
        # se o resto da divisão é zero, adiciona
        # divisor na lista
        if numero % divisor == 0:
            divisores.append(divisor)

    return divisores


numero = 26

print(divisores(numero))
