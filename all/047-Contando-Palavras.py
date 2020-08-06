"""Exercício 47"""


from string import punctuation

def contando_palavras(texto: str):
    # separa o texto em palavras
    texto = texto.split(" ")
    palavras = {}  # inicializa dicionário
    # para cada palavra na lista de palavras
    for palavra in texto:
        # se nâo é um sinal de pontuação ou um espaço
        if not (palavra in punctuation or palavra == " "):
            palavra = palavra.lower()  # normaliza variável
            # se a palavra já foi adicionada no dicionário,
            # incrementa seu valor. Senão, adiciona no dict.
            if palavra in palavras.keys():
                palavras[palavra] += 1
            else:
                palavras[palavra] = 1

    return palavras


text = "Oi oi OI   oi OI oi oI salve  , ! ? ~ . salve salve meu velho"
print(contando_palavras(text))
