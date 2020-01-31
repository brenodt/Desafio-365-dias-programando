"""Exercício 17:
Crie um programa que receba um texto, e que retorne esse texto invertido."""


def inverte_str(texto: str):
    lista = list(texto)
    lista.sort(reverse=True)

    texto = "".join(lista)
    return texto


def inverte(texto):
    return texto[::-1]


entrada = "amora"
print(inverte(entrada))

test = [0, 1, 2, 3, 4, 5]
print(test[::2])
