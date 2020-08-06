

def ache_o_numero(lista):
    # Utiliza listcomps para facilitar o processo de busca, mas a lista gerada sempre
    # terá apenas um elemento. Retorna esse elemento
    return [numero for numero in lista if lista.count(numero) % 2 != 0][0]

