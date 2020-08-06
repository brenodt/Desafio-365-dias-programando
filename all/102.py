

# importa a constante de letras do alfabeto do módulo string
from string import ascii_lowercase as letras

# Cria um dicionário usando o resultado da função zip()
# zip() cria um iterável de Tuplas, que agrega valores posicionais
# de dois iteráveis:
#   letras >> lista contendo todas as letras do alfabeto
#   range() >> Iniciando em 1, até o tamanho da lista de letras + 1
#
# O Resultado é um dicionário com o valor de cada letra do alfabeto
PONTOS = dict(zip(letras, range(1, len(letras) + 1)))

def maior_pontuação(texto: str):
    # Quebra o texto em palavras usando espaço como um separador
    # O resultado é uma lista de palavras
    palavras = texto.split(' ')
    
    # A seguinte listcomp executa a mesma lógica presente no seguinte bloco:
    #
    # pontuações = []
    # for palavra in palavras:
    #     pontos = 0
    #     for letra in palavra:
    #         pontos += PONTOS[letra]
    #     pontuações.append(pontos)
    pontuações = [sum([PONTOS[letra] for letra in palavra]) for palavra in palavras]
    
    # retorna a palavra no índice correspondente ao índice de pontuação máxima
    return palavras[pontuações.index(max(pontuações))]
