

def busca_linear(iteravel, valor):

    for indice in range(len(iteravel)):
        if iteravel[indice] == valor:
            return indice
    
    return -1