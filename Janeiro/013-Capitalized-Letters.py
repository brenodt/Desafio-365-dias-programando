"""Exercício 13:
cria um programa que receba uma string, e retorne essa mesma com todas as letras maiúsculas - sem usar o método .upper()
"""


from string import ascii_lowercase as lower, ascii_uppercase as upper


def to_uppercase(texto: str):
    saida = ""  # inicializando a variável de saída

    # verifica cada caractere
    for caractere in texto:
        # se caractere está presente em lower
        if caractere in lower:
            indice = lower.index(caractere)  # toma o índice da letra

            saida += upper[indice]  # adiciona a letra maiúscula na saída

        else:  # se o caractere já for maiúsculo ou pontuação
            saida += caractere

    return saida
