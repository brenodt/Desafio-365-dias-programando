
# Função auxiliar que implementa algoritmo similar à função clamp(), presente
# em outras linguagens como C++ e C#. 
# Parâmetros: 
#   n >> valor a ser analisado
#   valor_menor >> Mínimo valor possível
#   valor_maior >> Máximo valor possível
#
# Caso n seja menor que o valor_menor, retorna valor_menor.
# Caso n seja maior que o valor_maior, retorna valor_maior.
def clamp(n: int, valor_menor: int, valor_maior: int): return max(valor_menor, min(n, valor_maior))

def maiores_valores(lista: list, N: int):
    N = clamp(N, 1, len(lista))  # Normaliza N usando função auxiliar

    # Retorna uma nova lista ordenada de forma decrescente
    # com base no argumento. Utiliza notação de fatiamento
    # para retornar apenas os N primeiros elementos.
    # Lembrando que N é exclusivo, conforme lógica da notação.
    return sorted(lista, reverse=True)[:N]

if __name__ == "__main__":
    # Lista de referência
    lista_teste = [-2, 10, 5, 18, 3, -7, 0, 17, 14, -2, -10]
    n = -5  # N negativo << Impossível
    print(maiores_valores(lista_teste, n))
    # Saída: [18]
    # Com um n negativo, retorna apenas o maior elemento

    n = len(lista_teste) + 5  # N Maior que a lista << Impossível
    print(maiores_valores(lista_teste, n))
    # Saída: [18, 17, 14, 10, 5, 3, 0, -2, -2, -7, -10]
    # Com um n maior que o total da lista, retorna
    # a lista inteira, ordenada do maior ao menor

    n = 3  # N possível
    print(maiores_valores(lista_teste, n))
    # Saída: [18, 17, 14]
    # Caso n seja válido, retorna uma lista ordenada de n elementos



    