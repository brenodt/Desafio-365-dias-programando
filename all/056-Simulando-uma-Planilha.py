"""
Exercício 56:

Crie uma classe que cria uma planilha. 

* Armazene os dados em colunas e linhas
* Crie um método para imprimir uma linha
* Crie um método para imprimir uma coluna
* Crie um método para imprimir sua planilha no terminal

"""

from string import ascii_uppercase as upper

class Planilha():
    # PARA ADICIONAR ELEMENTOS À INSTÂNCIA, USA-SE A NOTAÇÃO
    # DE COLCHETES. Exemplo: Célula A0 == planilha['A'][0]
    def __init__(self, linhas=100, colunas=100):
        # Usando List Comprehension para criar um objeto iterável,
        # que é passado como argumento de um dict comprehension. 
        # Inicializo a planilha com 100 linhas e colunas (variável)
        # Inicialmente, as listas são compostas de objetos nulos (None)
        ls = [self.__coluna(numero) for numero in range(1, colunas + 1)]
        self.planilha = {key: [None] * linhas for key in ls}

    # CONVERSOR DE NÚMERO PARA LETRA DE COLUNA
    # Feito no exercício do dia 37
    def __coluna(self, letra: int):
        col = ''
        while letra > 0:
            indice = int((letra -1) % 26)
            col = upper[indice] + col
            letra = (letra - 1) // 26
        return col

    # usa o método print_linha() para imprimir a planilha completa.
    # Toma o tamanho da coluna A como referência, considerando que todas
    # as colunas tem o mesmo tamanho.
    def print_planilha(self):
        tamanho = len(self.planilha['A'])
        contador = 0
        while contador <= tamanho:
            self.print_linha(contador)
            contador += 1

    def print_linha(self, indice:int = 0):
        string = ''  # inicializa variável
        # caso seja passado 0, considere o cabeçalho
        if indice == 0:
            head = self.planilha.keys()
            for elemento in head:
                string += elemento + '   '
        elif indice > 0:
            for celula in self.planilha.values():
                string += str(celula[indice - 1]) + '  '
        print(string)

    def print_coluna(self, coluna:str):
        try:
            col = self.planilha[coluna]
            print(coluna)
            for elemento in col:
                print(elemento)
        except KeyError:
            print("Coluna fora do alcance.")          

p = Planilha(5, 5)
p.planilha['A'][4] = 10
p.print_planilha()
# --------- OUTPUT: ----------
# 
# A   B   C   D   E
# None  None  None  None  None
# None  None  None  None  None
# None  None  None  None  None
# None  None  None  None  None
# 10  None  None  None  None
