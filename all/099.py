

from collections import Counter
def elemento_mais_repetido(lista):
    #      !----- Sitaxe concisa, que resume o seguinte processo: -----!
    #
    # 1: organizar a lista de entrada. sorted organiza do menor para o maior.
    #    Usamos o argumento opcional "reverse=True" para inverter a saída.
    # >> lista_corrigida = sorted(lista, reverse=True)
    #
    # 2: Instanciar um objeto Counter(). Counter é uma sub-classe de dict,
    #    que usa elementos de um iterável como chaves, e o número de ocorrências
    #    desse elemento como o valor atrelado a essa chave.
    #    *Nota*: Organizar a lista de entrada só funciona pois, à partir de Python 3.7,
    #            o objeto Counter herda da classe dict a capacidade de lembrar da ordem
    #            de inserção dos elementos. Versões anteriores não possibilitavam isso.
    # >> contador = Counter(lista_corrigida)
    #
    # 3: Usar o método most_common() da classe Counter() para encontrar o elemento mais
    #    repetido. most_common() pode ou não ter um argumento especificando quantos ele-
    #    mentos queremos. Retorna uma lista de tuplas, do elemento com mais ocorrências
    #    até o menor. Cada tupla contém (elemento, número de ocorrências)
    # >> mais_comuns = contador.most_common()
    #
    # 4: Retornar o elemento mais repetido. Ele estará na primeira tupla, na primeira
    #    posição. Acessar o elemento usando sintaxe de fatiamento.
    # >> return mais_comuns[0][0]

    return Counter(sorted(lista, reverse=True)).most_common()[0][0]