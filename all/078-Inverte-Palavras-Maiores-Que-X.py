def spin_words(sentence):
    words = sentence.split(" ")  # Creates List containing each word
    lens = [len(word) for word in words]  # Aux. List w/ all lenghts
    # For each word in list
    for index in range(len(words)):
        if lens[index] >= 5:  # For words w/ 5 or more chars
            word = words[index]  # saves pointer for current word
            words[index] = word[::-1]  # Replaces the words in list reversed
    return " ".join(words)  # Joins all words in list with spaces between them



def inverte_palavras(texto, valor):
    # De dentro para fora:
    # 1: Separa as palavras em um iterável usando .split(" ")
    # 2: Usa compreensão de lista para iterar cada palavra
    # 3: Usa operador ternário para avaliar a condição e retornar dois valores possíveis;
    #    'Palavra invertida' se o tamanho for maior que valor, senão retorna 'Palavra'
    # 4: Usa fatiamento para inverter a str. [inicio:fim:passo] => Passo -1 inverte o texto
    # 5: Usa " ".join() para criar um texto único, contendo espaço entre as palavras
    return " ".join([palavra[::-1] if len(palavra) >= valor else palavra for palavra in texto.split(" ")])
