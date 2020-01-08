"""Exercício 8:
Escreva uma função que receba dois números inteiros (a e b), e retorne uma lista contendo todos os números inteiros cujos dígitos são todos pares (a e b inclusos)"""


def digitos_pares(valor_inicial: int = 0, valor_final: int = 1000):
    saida = []

    # usando (valor final + 1) pois a função range não inclui o valor final por definição
    for numero in range(valor_inicial, valor_final + 1):
        digitos_str = str(numero)

        check = True  # essa variável se manterá como True se todos os digitos forem positivos
        for digito in digitos_str:
            if int(digito) % 2 != 0:  # usando operador modulo pra determinar se o número é par
                check = False
                break  # após o primeiro dígito ímpar, sai do for loop

        if check:  # se o número é par, adiciona ele à lista
            saida.append(numero)

    return saida


inicio = 0
fim = 30
print(digitos_pares(inicio, fim))
