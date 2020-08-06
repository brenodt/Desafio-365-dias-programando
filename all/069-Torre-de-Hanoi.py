def torre_de_hanoi(n , de_haste, para_haste, haste_auxiliar): 
    # Condição de
    if n == 1: 
        print(f"Mova o disco 1 da haste {de_haste} para haste {para_haste}")
        return  # retorna None, é simplesmente uma maneira de terminar a função
    
    # Aqui inicia o processo recursivo
    # Faz o movimento considerando a haste final como auxiliar
    torre_de_hanoi(n-1, de_haste, haste_auxiliar, para_haste) 
    print(f"Mova o disco {n} da haste {de_haste} para {para_haste}")
    # Move a peça para a haste final
    torre_de_hanoi(n-1, haste_auxiliar, para_haste, de_haste)

