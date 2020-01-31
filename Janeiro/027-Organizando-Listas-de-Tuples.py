"""Exercício 27:
Dada uma lista contendo tuples de três elementos: Nome, Idade, Empregado

Organize a lista em relação a cada um dos elementos
"""


minha_lista = [("Andre Piva", 23, True), ("Sandra Grigol", 29, True),
               ("Leoncio Ramos", 47, False), ("Norman Jacques", 34, False),
               ("Marcel Proust", 20, True), ("Didier Deschamps", 56, False)]


for indice in range(0, 3):
    # no método sort abaixo, o parâmetro key recebe uma função lambda como argumento,
    # que retorna como critério de organização (a chave) um item de um dado índice
    minha_lista.sort(key=lambda minha_tuple: minha_tuple[indice])
    print(minha_lista)
    # -- OUPUT: --
    # Primeira iteração (índice 0):
    # [('Andre Piva', 23, True), ('Didier Deschamps', 56, False), ('Leoncio Ramos', 47, False),
    # ('Marcel Proust', 20, True), ('Norman Jacques', 34, False), ('Sandra Grigol', 29, True)]
    #
    # Segunda iteração (índice 1):
    # [('Marcel Proust', 20, True), ('Andre Piva', 23, True), ('Sandra Grigol', 29, True),
    # ('Norman Jacques', 34, False), ('Leoncio Ramos', 47, False), ('Didier Deschamps', 56, False)]
    #
    # Terceira iteração (índice 2):
    # [('Norman Jacques', 34, False), ('Leoncio Ramos', 47, False), ('Didier Deschamps', 56, False),
    # ('Marcel Proust', 20, True), ('Andre Piva', 23, True), ('Sandra Grigol', 29, True)]

