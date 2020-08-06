
# Exemplo extraído da documentação de Python, em:
# https://docs.python.org/3/library/bisect.html
from bisect import bisect

def nota(ponto, intervalos=[60, 70, 80, 90], notas='FDCBA'):
    # Encontra o índice onde a nota se encaixa,
    # em um intervalo ordenado! Bisect acha a 
    # posição onde o valor deve ser inserido,
    # a fim de manter a ordem dos elementos.
    indice = bisect(intervalos, nota)  
    # Retorna a nota equivalente
    return notas[indice]

