


def segunda_menor(lista: list):
    # Organiza a lista em ordem descendente,
    # com base na nota (posição 2 da sub-string)
    # [[Nome, Maior Nota], [Nome, Segunda Maior], ... , [Nome, Menor Nota]]
    lista.sort(key=lambda x: x[1], reverse=True)
    
    penultimo = None  # inicializa variável
    i = len(lista) - 1  # i é o índice de referência
    while True:
        if lista[i][1] != lista[-1][1]:
            # Econtrada a segunda menor nota
            # Armazena a sub-lista como referência
            penultimo = lista[i]
            break
        i -= 1
        if i < 0:
            return -1  # caso todos os elementos sejam iguais, retorna -1
    # Cria uma nova lista contendo apenas os nomes de alunos
    # que tiraram a menor nota. Isso adressa a possibilidade
    # de mais de um aluno ter tirado essa nota
    nova_lista = [x[0] for x in lista if x[1] == penultimo[1]]
    
    # Caso haja mais de um aluno, organiza a lista em ordem alfabética
    if len(nova_lista) > 1:
        nova_lista.sort()

    for el in nova_lista:
        # printa cada nome no terminal
        print(el)


l = [['Harry', 37.21], ['Berry', 37.21], ['Tina', 37.2], ['Akriti', 41], ['Harsh',39]]
m = [['Harsh', 20], ["Beria", 20], ['Varun', 19], ['Kakunami', 19], ['Vikas', 21]]
segunda_menor(m)
