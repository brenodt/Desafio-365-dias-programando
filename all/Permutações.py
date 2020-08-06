
from itertools import permutations 


def acha_permutacoes(texto: str): 
     # retorna todas permutações possíveis 
     return permutations(texto) 

        
# Programa Principal
if __name__ == "__main__": 
    texto: str = 'devdiario'
    perm_list = acha_permutacoes(texto)
    # printa todas as permutações no terminal 
    for perm in list(perm_list): 
        print (''.join(perm))



