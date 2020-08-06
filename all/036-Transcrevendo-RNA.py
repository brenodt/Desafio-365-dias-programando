"""Exercício 36:
Transforme uma determinada sequência de DNA, retorne seu RNA complementar.

G > C
C > G
T > A
A > U
"""


def RNA(dna: str):
    dna = dna.upper()  # normaliza a entrada
    rna = ""  # inicializa variável
    for letra in dna:
        # uso elif para evitar redundância;
        # impede que uma letra que ja foi
        # determinada continue sendo validada
        if letra == "G":
            rna += "C"
        elif letra == "C":
            rna += "G"
        elif letra == "T":
            rna += "A"
        elif letra == "A":
            rna += "U"
    return rna
