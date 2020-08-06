

from collections import OrderedDict  # OrderedDict deve ser importado!

def enesimo_nao_repetido(entrada: str, n: int):
    # Cria o dicionário usando OrderedDict e inicializa
    # cada chave com o valor 0
    dicionario = OrderedDict.fromkeys(entrada, 0)

    # Conta a ocorrência de cada letra
    for letra in entrada:
        dicionario[letra] += 1

    # Usando List Comprehension, elimina letras duplicadas
    elementos_nao_repetidos = [ chave for (chave, valor) in \
        dicionario.items()if valor == 1 ]

    # Se N é maior do que o número de letras não repetidas
    if len(elementos_nao_repetidos) < n:
        return -1
    else:  # Senão, retorne a n-ésima letra não repetida
        return elementos_nao_repetidos[n-1]


if __name__ == "__main__":

    texto = "AA BB CC DD EE F GG H II JJ KK L M N OO"
    letra = 5

    # -- SAÍDA --:
    # N
    print(enesimo_nao_repetido(texto, letra))