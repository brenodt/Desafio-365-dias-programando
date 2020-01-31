"""Exercício 18:
Crie duas funções que calculem o fatorial de um número N. Uma utilizando recursão e ou não."""



def fatorial_recursivo(numero: int):
    if not numero:  # se número == 0; 0 é falsy então retorna negativo
        return 1
    # senão, retorne o número * o fatorial do anterior
    return numero * fatorial_recursivo(numero - 1)


def fatorial(numero: int):
    fatorial = 1  # inicializa variável
    while numero != 0:
        fatorial *= numero  # declaração abreviada
        numero -= 1

    return fatorial
