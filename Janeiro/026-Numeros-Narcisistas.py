"""Exercício 26:
Determine se um número é um número narcisista.
Pela definição, um número é narcisista se a soma de seus dígitos elevados pelo número de dígitos é igual a ele mesmo

9 é narcisista: (9 ** 1) = 9
153 é narcisista: (1 ** 3 = 1) + (5 ** 3 = 125) + (3 ** 3 = 27) = 153
370 é narcisista
"""


def narcisista(numero: int):

    string_do_numero = str(numero)

    numero_de_digitos = len(string_do_numero)

    soma = 0
    for digito in string_do_numero:
        soma += int(digito) ** numero_de_digitos

    if soma == numero:
        return f"{numero} é Narcisista."
    return f"{numero} não é Narcisista."
