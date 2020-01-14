"""Exercício 14:
Dada uma lista desordenada de valores, econtre um par de números que, somados, resultem em um número dado.
Crie uma função que receba a lista e o número-alvo. Retorne uma tuple com o par encontrado.
"""

def ache_par(lista: list, numero: int):
    # ordena a lista de maneira ascendente
    lista.sort()

    # armazena os índices do número menor e maior
    menor = 0
    maior = len(lista) - 1

    # se o índice menor é igual ao maior, não há
    # par que satisfaça a condição 
    while menor != maior:
        # soma dos valores nos índices indicados
        soma = lista[menor] + lista[maior]

        if soma == numero:
            return lista[menor], lista[maior]  # retorna uma tuple contendo os números
        
        # se a soma é menor que o alvo, incrementa o índice menor
        if soma < numero:
            menor += 1
        # se a soma é maior que o alvo, decrementa o índice maior
        else:
            maior -= 1
    # retorna -1 se não há par que satisfaça a condição
    return -1

