"""Exercício 10:
Dado um número X, gere um dicionário contendo os números 1 a X (inclusos), e seus respectivos quadrados."""


def gera_dicionario(numero: int = 10):
    return {x: x**2 for x in range(1, numero + 1)}
