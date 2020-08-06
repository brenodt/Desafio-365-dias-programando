'''
Write a method that takes an array of consecutive (increasing) letters as input and that returns the missing letter in the array.

You will always get an valid array. And it will be always exactly one letter be missing. The length of the array will always be at least 2.
The array will always contain letters in only one case.

Example:

['a','b','c','d','f'] -> 'e' ['O','Q','R','S'] -> 'P'

["a","b","c","d","f"] -> "e"
["O","Q","R","S"] -> "P"
'''

from string import ascii_lowercase as minusculas, ascii_uppercase as maiusculas

def encontre_a_letra(caracteres):
    # Cria um objeto slice que representa a porção de letras a serem avaliadas
    letras = slice(minusculas.index(caracteres[0].lower()), minusculas.index(caractere[-1].lower()))

    # Os caracteres recebidos podem ser uma lista de letras
    # maiúsculas ou minúsculas. Avalia qual das opções é a correta
    # para o argumento recebido
    if caracteres[0] in minusculas: # Caso caracteres sejam minúsculos
        letra_que_falta = [letra for letra in minusculas[letras] if letra not in caracteres]
    else:  # Caso caracteres sejam maiúsculos
        letra_que_falta = [letra for letra in maiusculas[letras] if letra not in caracteres]
        
    return letra_que_falta[0]  # Letra que falta é uma lista de len() == 1. Retorna seu único elemento

