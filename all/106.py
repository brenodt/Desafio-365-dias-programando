

def maior_sublista(lista):
    # Inicia os contadores do comprimento e o último
    # índice da sublista. O mínimo é uma sublista de um
    # elemento
    comprimento_sublista = 1
    indice_final = 0

    # contador que será incrementado quando a sublista
    # aumentar, baseado na mudança de sinais
    contador = 1

    # Inicia o loop à partir do segundo elemento. Sempre
    # compara o elemento atual com o anterior
    for indice in range(1, len(lista)):
        # Caso o elemento multiplicado pelo anterior seja
        # menor do que zero, os sinais alternaram
        if lista[indice] * lista[indice - 1] < 0:
            contador += 1  # incrementa o contador

            # Caso o contador seja maior que o comprimento
            # da atual maior sublista
            if contador > comprimento_sublista:
                # Novo comprimento é igual ao contador,
                # novo índice final é o índice atual
                comprimento_sublista = contador
                indice_final = indice
        else:
            contador = 1  # reinicia o contador
    
    # Índice inicial = índice final - comprimento encontrado
    #
    # Somar 1 ao índice inicial para compensar índice 0
    # Somar 1 ao índice final pois na notação de fatiamento o fim é exclusivo
    return lista[(indice_final - comprimento_sublista) + 1:indice_final + 1]


print(maior_sublista([1, -2, 6, -1, 7, -14, 2, 4, -3, 2, -4, -3, 1, -5, 2, -10, 6]))