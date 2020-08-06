


def separa_e_une(texto: str):
    # separa o texto usando espaço como
    # limitador para cada elemento
    texto_separado = texto.split(' ')

    # o novo texto será a união das palavras
    # encontradas, agora separadas por um traço
    texto_corrigido = '-'.join(texto_separado)
    # retorna cada um dos elementos encontrados
    return texto_separado, texto_corrigido