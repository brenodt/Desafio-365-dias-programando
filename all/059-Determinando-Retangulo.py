from math import sqrt

def distancia_entre_dois_pontos(ponto1: tuple, ponto2: tuple):
    
    x = (ponto2[0] - ponto1[0]) ** 2
    y = (ponto2[1] - ponto1[1]) ** 2

    return sqrt(x + y)

def verifica_se_retangulo(pontos: list):
    '''
    Determina se 4 pontos são um retângulo.
    Retorna 1 caso as validações sejam verdadeiras,
    Retorna 0 caso não sejam.
    '''
    A, B, C, D = pontos

    AB = distancia_entre_dois_pontos(A, B)
    CD = distancia_entre_dois_pontos(C, D)
    if AB == CD:
        AD = distancia_entre_dois_pontos(A, D)
        BC = distancia_entre_dois_pontos(B, C)
        if AD == BC:
            AC = distancia_entre_dois_pontos(A, C)
            BD = distancia_entre_dois_pontos(B, D)
            if AC == BD:
                return 1
    return 0

