

## >> OPÇÃO 1 <<
def é_fibonacci_01(n):
    x = 0  # índice 0
    y = 1  # índice 1
    indice = 1  # contador

    while True:
        indice += 1  # incrementa contador

        # se o índice é par, modifica x,
        # senão, modifica y
        if indice % 2 == 0:
            x = x + y
        else:
            y = x + y
            
        if n == x or n == y:  # se n é igual a x ou y
            return True  # n é um número de Fibonacci
        elif n < x or n < y:  # se n é menor que x ou y
            return False  # x ou y passaram por n, portanto não é

## >> OPÇÃO 2 <<
from math import sqrt as raiz_quadrada
  
# Função para encontrar um quadrado perfeito x
# Retorna verdadeiro se é um quadrado perfeito
def quadrado_perfeito(x): 
    n = int(raiz_quadrada(x))  # converte o resultado para int(). Inicialmente é float
    if n ** 2 == x:  # se n ao quadrado é igual a x
        return True  # é um quadrado perfeito
    return False
  
# Função que retorna verdadeiro se n é um número de Fibonacci
def é_fibonacci_02(n):
    # um número faz parte da sequência de Fibonacci se (5 * (n ** 2) + 4) ou
    # (5 * (n ** 2) - 4) são um quadrado perfeito.
    return quadrado_perfeito(5 * (n ** 2) + 4) or quadrado_perfeito(5 * (n ** 2) - 4)