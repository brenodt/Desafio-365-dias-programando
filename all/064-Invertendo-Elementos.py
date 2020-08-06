

def Inverte_Elementos(lista: list): 
    
    lista[0], lista[-1] = lista[-1], lista[0] 
  
    return lista


l = [0, 1,2,3,4,5,6]
print(Inverte_Elementos(l))