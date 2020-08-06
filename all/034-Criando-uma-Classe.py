"""Exercicio 34:
Crie uma classe com dois metodos, pelo menos:
recebe_string(): para pegar do console um texto
printa_string(): para imprimir a string no console
"""

class IOTexto():
    def __init__(self):
        self.texto = ""

    def recebe_string(self):
        self.texto = input("Defina o texto: ")

    def printa_string(self):
        print(f"Seu texto guardado: \n{self.texto}")


minha_instancia = IOTexto()

minha_instancia.recebe_string()
minha_instancia.printa_string()