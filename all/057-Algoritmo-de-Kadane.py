


def sublista_maior(lista):
    """Encontra a sublista contígua de soma máxima"""
    maior_soma = 0
    inicio_sublista = fim_sublista = 0
    soma_atual = 0
    for fim_atual, x in enumerate(lista):
        if soma_atual <= 0:
            # Caso a soma seja negativa, reseta a contagem
            # e reinicia o posicionamento da sub-lista
            inicio_atual = fim_atual
            soma_atual = x
        else:
            # Senão, aumenta a soma atual
            soma_atual += x

        if soma_atual > maior_soma:
            # Caso a soma atual tenha passado a melhor já encontrada
            # substitue a melhor
            maior_soma = soma_atual
            inicio_sublista = inicio_atual
            fim_sublista = fim_atual + 1  # o +1 torna 'fim_sublista' exclusivo
    # como notação slicing em Python é [inclusivo:exclusivo], torno o 'fim_sublista' exclusivo
    # Retorno uma tuple contendo a soma, e a sub-lista
    return maior_soma, lista[inicio_sublista:fim_sublista]


t = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
# ----- OUTPUT -----
# (6, [4, -1, 2, 1])
print(sublista_maior(t))
