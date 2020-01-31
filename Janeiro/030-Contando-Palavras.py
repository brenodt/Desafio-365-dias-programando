"""Exercício 30:
Dada uma string, descubra quantas palavras essa string possui.
"""


def numero_de_palavras(texto: str):
    lista = texto.split(sep=" ")
    palavras = [palavra for palavra in lista if palavra != ""]
    return len(palavras)
