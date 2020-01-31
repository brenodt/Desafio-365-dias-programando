"""Exercício 19:

Dada uma string qualquer, retorne o número de letras e números presentes nela. Retorne uma tuple contendo o resultado."""


from string import ascii_letters, digits


def conta_letra_numero(texto: str):
    # inicializa contadores
    numeros = 0
    letras = 0

    # avaliando cada char presente no texto
    for caractere in texto:
        if caractere in ascii_letters:  # se faz parte da constante de letras
            letras += 1

        # usando elif para aumentar a eficiência. Se é
        # letra, não será número, então a validação não
        # precisa acontecer.
        elif caractere in digits:  # se é um número
            numeros += 1

    return letras, numeros
