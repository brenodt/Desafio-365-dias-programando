from string import ascii_uppercase as upper


def coluna_excel(letra: int):
    coluna = ""  # inicializa a variável
    while letra > 0:
        # 26 letras, porém a lista inicia no índice 0
        indice = int((letra - 1) % 26)
        # adiciona a nova letra sempre a esquerda,
        # como seria a escrita de um número maior
        coluna = upper[indice] + coluna
        
        # reduz a letra na base 26. Divisão inteira,
        # sem as casas decimais
        letra = (letra - 1) // 26




