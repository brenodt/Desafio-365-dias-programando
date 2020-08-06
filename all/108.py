def isola_impar(num):
    if num is None: return 'None'
    
    num = str(num) # Converte para texto
    out = []  # Inicializa lista de saída
    i = 0  # Contador de índice
    
    while i < len(num):
        if num[i] != '-':
            if int(num[i]) % 2 != 0:
                out.append('-')
                out.append(num[i])
                out.append('-')
            else:
                out.append(num[i])
        
        i += 1
    
    # Elimina traços duplicados
    i = 1
    while i < len(out):
        if out[i] == '-' and out[i - 1] == '-':
            out.pop(i)
        i += 1
            
    out = ''.join(out)
    return out.strip('-')

