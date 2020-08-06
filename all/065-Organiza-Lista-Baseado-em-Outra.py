


def organiza_lista(lista: list, ordem: list): 
    if len(lista) != len(ordem):  # impossível de organizar
        return
    # cria uma lista de tuples contendo elementos das
    # listas originais    
    elementos_zipados = zip(lista, ordem)

    # organiza em relação ao segundo elemento de cada tuple
    elementos_organizados = sorted(elementos_zipados, key=lambda x: x[1])
    # extrai dos elementos organizados o primeiro item de cada tuple
    return [x[0] for x in elementos_organizados]
    


# driver code 
x = ["a", "b", "c", "d", "e", "f", "g", "h", "i"] 
y = [ 0,   1,   1,   0,   1,   2,   2,   0,   1] 
print(organiza_lista(x, y))
