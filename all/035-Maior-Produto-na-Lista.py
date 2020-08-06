"""Exercício 35:
Determine o maior produto entre dois elementos de uma lista. Retorne os elementos
"""


def quicksort(lista: list):
    # condição de parada
    if len(lista) <= 1:
        return lista
    # referência é o elemento do meio da array
    pivo = lista[len(lista) // 2]
    # cria três sub arrays
    menor = [item for item in lista if item < pivo]
    igual = [item for item in lista if item == pivo]
    maior = [item for item in lista if item > pivo]
    # recursão nas sub arrays menores e maiores
    return quicksort(menor) + igual + quicksort(maior)
    

def maior_produto(lista: list):
    # organiza a lista recebida
    lista = quicksort(lista)
    # ou os dois primeiros elementos serão o
    # maior produto, ou os dois últimos
    primeiro_par = lista[0] * lista[1]
    ultimo_par = lista[-1] * lista[-2]

    if primeiro_par > ultimo_par:
        return lista[0], lista[1]
    if primeiro_par < ultimo_par:
        return lista[-2], lista[-1]
    
    # se o resultado das duas multiplicações é igual
    return (lista[0], lista[1]), (lista[-2], lista[-1])


minha_lista = [-3, -10, 5, 6, -2]
maior = maior_produto(minha_lista)
print(maior)
