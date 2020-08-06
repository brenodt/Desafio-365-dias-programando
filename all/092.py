

# Exemplo de entrada
entrada = ["a", "aa", "Essa", "Daqui", "aa", "aaaaa", "a"]
n = 2  # número de palavras consecutivas a serem verificadas

def maior_palavra_consecutiva(entrada, n):
    # armazena o tamanho da lista de entrada em uma variável
    tamanho_da_entrada = len(entrada)  
    if 0 <= tamanho_da_entrada < n or n <= 0: return ""  # eliminando valores que não devem ser considerados

    # Gera uma lista onde cada sub-lista contém N palavras;
    # Exemplo: 
    # entrada = ["a", "b", "c", "d"]  >> sublistas = [["a", "b"], ["b", "c"], ["c", "d"]]
    sublistas = [entrada[i:i+n] for i in range(tamanho_da_entrada)]

    # Cria uma lista onde cada elemento é uma str concatenada para cada sublista da entrada;
    # Exemplo:
    # sublistas = [["a", "b"], ["b", "c"], ["c", "d"]] >> palavras = ["ab", "bc", "cd"] 
    palavras = ["".join(sublista) for sublista in sublistas]

    # Retorna a maior palavra, usando a função max(), que recebe como chave de comparação o resultado da função len(s)
    return max(palavras, key=len)

print(maior_palavra_consecutiva(entrada, n))
# SAIDA:
# EssaDaqui