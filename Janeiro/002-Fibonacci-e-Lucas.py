"""Essa função encontra o valor do número de índice X (primeiro argumento),
   dados F1 e F2 (valor padrão => 0 e 1 : Fibonacci)
"""


def value_of_index(index: int, f1=0, f2=1):
    if index == 0:
        return f1
    elif index == 1:
        return f2
    else:
        value = 0
        for i in range(1, index):
            value = f1 + f2
            f1 = f2
            f2 = value
        return value
