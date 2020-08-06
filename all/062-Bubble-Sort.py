
def bubbleSort(lista: list): 
    n = len(lista)  # tamanho da lista recebida
   
    # Atravessa cada um dos elementos na lista
    for i in range(n): 
        swapped = False  # variável de controle do loop
  
        # Considerando que o último elemento 'i' já está
        # no lugar (o código no loop interno garante isso)
        for j in range(0, n-i-1): 
            # atravessa a lista de 0 até n-i-1.
            # Inverte os elementos se o achado
            # é maior que o próximo elemento
            if lista[j] > lista[j+1] : 
                lista[j], lista[j+1] = lista[j+1], lista[j] 
                swapped = True  # Indica que houve mudança
  
        # Caso não tenha havido nenhuma mudança no loop
        # interno, a lista já está ordenada!
        if swapped == False: 
            break


l = [64, 34, 25, 12, 22, 11, 90, 10]
bubbleSort(l)
print(l)
