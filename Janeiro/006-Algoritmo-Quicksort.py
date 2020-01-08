def quicksort(entrada: list):
    # condição de parada!
    if len(entrada) <= 1:
        return entrada

    # escolhe o valor do meio como pivô
    pivo = entrada[len(entrada) // 2]

    # uso de list comprehension é o jeito mais pythonico de fazer as verificações
    # adiciona na sub menor se x é menor que o pivo
    subarray_menor = [x for x in entrada if x < pivo]
    # adiciona na sub do meio se x é igual ao pivo
    meio = [x for x in entrada if x == pivo]
    # adiciona na sub maior se x é maior que o pivo
    subarray_maior = [x for x in entrada if x > pivo]

    # chama a própria função no return statement >> recursão!
    return quicksort(subarray_menor) + meio + quicksort(subarray_maior)


minha_lista = [9, -3, 5, 2, 6, 8, -6, 1, 3]
lista_organizada = quicksort(minha_lista)

print(lista_organizada)
