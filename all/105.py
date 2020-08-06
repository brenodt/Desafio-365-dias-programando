

from collections import Counter

def palavras_possiveis(dicionario, letras):
    saida = []

    for palavra in dicionario:
        possivel = True

        contador = Counter(palavra)
        for letra in contador.keys():
            if letra not in letras:
                possivel = False
            else:
                if letras.count(letra) < contador[letra]:
                    possivel = False
            
        if possivel:
            saida.append(palavra)
    
    return saida


if __name__ == "__main__":
    entrada = ['oi', 'boi', 'frajola', 'frango', 'aroma', 'amora',] 
    letras = ['a', 'o', 'o', 'a', 'm', 'r', 'l', 'i'] 
    possiveis = palavras_possiveis(entrada, letras)
    print(possiveis)  # Saída: ['oi', 'aroma', 'amora']