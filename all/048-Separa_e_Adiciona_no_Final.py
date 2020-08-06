def separa_e_adiciona(lista: list, pos_do_corte: int):
    # se é um índice positivo executa
    if pos_do_corte >= 0:
        # usa-se list slicing para tomar a parte cortada
        parte_cortada = lista[:pos_do_corte]
        # e a parte restante
        saida = lista[pos_do_corte:]
        # adiciona cada elemento cortado ao final da lista
        for elemento in parte_cortada:
            saida.append(elemento)
        return saida


lista = [1, 2, 3, 4, 5, 6, 7]

indx = 1

print(separa_e_adiciona(lista, indx))
