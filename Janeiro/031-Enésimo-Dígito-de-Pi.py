"""Exercício 31:
Entrar com um número e gerar Pi com o dado número de casas decimais. Coloque um limite de casas decimais!
"""

from decimal import getcontext, Decimal


def pi(digitos_desejados: int):
    i = 1  # contador de iterações

    # aumenta dois no tamanho pois deve contabilizar
    # o "3" do valor numérico e o fato de que o último
    # dígito sempre será uma aproximação
    tamanho = digitos_desejados + 2

    # define a precisão para o tamanho estipulado
    getcontext().prec = tamanho
    # retira o arredondamento do algoritmo, pois
    # o número já vem correto, não precisa ser arredondado
    getcontext().rounding = "ROUND_FLOOR"

    # >> Aqui começa o algoritmo de Gauss-Legendre <<
    # valores iniciais das quatro variáveis
    a0 = Decimal(1)
    b0 = Decimal(1 / Decimal(2).sqrt())
    t0 = Decimal(1 / 4)
    p0 = Decimal(1)

    # o número de dígitos corretos é igual ao número de iterações * 2
    # enquanto o tamanho estipulado é maior que o número de digitos corretos
    while i * 2 < tamanho:
        # define as variáveis com base nos valores iniciais OU anteriores
        a1 = Decimal((a0 + b0) / 2)
        b1 = Decimal(a0 * b0).sqrt()
        t1 = Decimal(t0 - p0 * ((a0 - a1) ** 2))
        p1 = Decimal(2 * p0)

        # redefine valores iniciais/anteriores com os novos
        a0 = a1
        b0 = b1
        t0 = t1
        p0 = p1

        i += 1

    # Pi é igual a fórmula definida
    pi = Decimal(((a1 + b1) ** 2) / (4 * t1))
    # como o último dígito está sempre aproximado, calculo 1 a mais do pedido
    # e retiro ele usando a função format()
    # dando n dígitos significativos
    return format(pi, f".{tamanho - 1}g")

