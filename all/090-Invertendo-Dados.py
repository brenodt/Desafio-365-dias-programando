# A stream of dados is received and needs to be reversed.

# Each segment is 8 bits long, meaning the order of these segments needs to be reversed, for example:

# 11111111  00000000  00001111  10101010
#  (byte1)   (byte2)   (byte3)   (byte4)
# should become:

# 10101010  00001111  00000000  11111111
#  (byte4)   (byte3)   (byte2)   (byte1)
# The total number of bits will always be a multiple of 8.

# The dados is given in an listaay as such:

# [1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,0,1,0,1,0,1,0]

def separa_bytes(lista, fator=8):
    # Utiliza yield para fatiar a lista de bits em bytes
    for indice in range(0, len(lista), fator):
        yield lista[indice:indice + fator]

def inverte_dados(dados):
    # O resultado de separa_bytes() é um gerador.
    # Transforma em lista usando o construtor. O resultado é
    # invertido usando notação de fatiamento. [início:fim:passo]
    dados = list(separa_bytes(dados))[::-1]
    # Usa listcomp composta para extrair de cada sub-lista (lista de 8-bits, bytes)
    # os bits, retornando apenas uma lista contendo os bits.
    return [elemento for sub_lista in dados for elemento in sub_lista]
