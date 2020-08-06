
# a função atualiza a lista sem retornar valores;
# ela modifica a instância diretamente
def mergeSort(lista: list):
    # enquanto a lista tiver, no mínimo
    # dois elementos
    if len(lista) > 1:
        # separa a lista em duas partes
        esquerda, direita = divide(lista)

        # executa o mesmo processo de ordenação,
        # chamando de maneira recursiva a função
        mergeSort(direita)
        mergeSort(esquerda)
        # contadores das listas esquerda,
        # direita e lista original, respectivamente
        i = j = k = 0
        
        # enquanto os dois contadores forem menores
        # que o tamanho das listas esquerda e direita,
        # altera o valor da posição da lista original
        # pelo maior valor da comparação entre o elemento
        # da direita e o da esquerda. Incrementa os contadores
        while i < len(esquerda) and j < len(direita):
            if esquerda[i] < direita[j]:
                lista[k] = esquerda[i]
                i += 1
            else:
                lista[k] = direita[j]
                j += 1
            k += 1
        
        # IMPORTANTE: se qualquer um dos
        # contadores se tornar maior que
        # o tamanho da respectiva lista,
        # o loop terminará. É por isso 
        # que adicionamos o restante da
        # na original (caso ainda haja)
        while i < len(esquerda):
            lista[k] = esquerda[i]
            i += 1
            k += 1
        while j < len(direita):
            lista[k] = direita[j]
            j += 1
            k += 1

# função ajudante, toma uma lista
# e divide em duas pela metade
def divide(lista: list):
    metade = len(lista) // 2
    parte_A = lista[:metade]
    parte_B = lista[metade:]

    return parte_A, parte_B


# Código de teste
if __name__ == "__main__":    
    lista = [3, 4, 2, 1, 7, 5, 8, 9, 0, 6]
    mergeSort(lista)
    print(lista)  # Output: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
