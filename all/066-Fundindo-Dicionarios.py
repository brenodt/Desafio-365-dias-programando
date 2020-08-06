


def funde_dicionarios(dic1: dict, dic2: dict): 
    # usando **kwargs (notação double star)
    # um novo dicionário é criado, fundindo
    # os dados dos dicionários 1 e 2, sem
    # alterar os dados desses argumentos
    novo_dicionario = {**dic1, **dic2} 
    return novo_dicionario


