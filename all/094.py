

# Opção 1:
def conta_caracteres1(texto):
    return {indice : texto.count(indice) for indice in texto}


# Opção 2:
from collections import Counter

def conta_caracteres2(texto):
    return Counter(texto)