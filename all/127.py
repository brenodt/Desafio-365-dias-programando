
from string import ascii_lowercase as letras

def espelha_palavra(palavra: str):
    lista_de_letras_espelhadas = []
    for c in palavra.lower():
        if c in letras:
            indice_espelhado = -letras.index(c) - 1

            letra_espelhada = letras[indice_espelhado]
            lista_de_letras_espelhadas.append(letra_espelhada)
        else:
            lista_de_letras_espelhadas.append(c)

    palavra_espelhada = ''.join(lista_de_letras_espelhadas)
    return palavra_espelhada


def sintaxe_reduzida(palavra: str):
    return ''.join([letras[-letras.index(c) - 1] if (c in letras) else c for c in palavra.lower()])

if __name__ == "__main__":
    
    p = "Hello World!"

    # Saída: svool dliow!

    espelho = espelha_palavra(p)
    print(espelho)
    espelho = sintaxe_reduzida(p)
    print(espelho)

