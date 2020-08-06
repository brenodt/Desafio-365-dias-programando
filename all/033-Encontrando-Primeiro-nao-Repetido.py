"""Exercicio 33:
Dada uma string encontre o primeiro caractere que nao se repete.
"""


def nao_repete(texto: str):
    # List comprehension onde cada letra cuja soma de ocorrencias 
    # e igual a um sera adicionada na lista
    letras = [letra for letra in texto if texto.count(letra) == 1]
    # retorna o primeiro indice da lista
    return letras[0]


nao_repete("abaBbBCccdECEg")