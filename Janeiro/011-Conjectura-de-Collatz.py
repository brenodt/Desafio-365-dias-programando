"""Exercício 11:
Crie um algoritmo que execute os passos definidos na conjectura de Collatz, definidos abaixo:
1: Comece com um número n > 1
2: Encontre o número de Passos necessários pra chegar em 1
3: Se n é par, divida por 2
4: Se n é ímpar, multiplique por 3 e adicione 1
"""


def conjectura_collatz(n: int):
    if n <= 1:
        return "O número deve ser maior que 1."
    passos = 0
    while n > 1:
        if n % 2 == 0:  # se o número é par
            n /= 2
        else:
            n = n * 3 + 1
        passos += 1

    return passos


print(conjectura_collatz(5))
