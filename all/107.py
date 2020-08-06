

from collections import Counter 
  
def maior_subgrupo_de_anagramas(palavras: list):

    # Para cada palavra da entrada, organizar as letras em ordem alfabética => padroniza
    # as palavras, de forma que anagramas serão iguais. Por usar sorted(), recebemos uma
    # lista de letras organizadas. Usamos join() para criar novamente uma str()
    palavras_organizadas = [''.join(sorted(palavras[i]))  for i in range(len(palavras))]
  
    # Criamos um dicionário contendo o tamanho de cada subgrupo de anagramas. As palavras
    # são usadas como chaves e o número de ocorrências é o valor associado à essa chave.
    tamanho_subgrupos = Counter(palavras_organizadas) 
  
    # Retorna o tamanho do maior subgrupo
    return max(tamanho_subgrupos.values())