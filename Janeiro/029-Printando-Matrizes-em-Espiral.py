"""Exercicio 29:
Dada uma matriz MxN, printe essa matriz no console em ordem espiral.
"""


class Espiral():
    def __init__(self, matriz):
        self.matriz = matriz
        # atributos de controle de limite impresso
        self.topo = 0
        self.fundo = len(self.matriz) - 1  # subtrai 1 para compensar o índice 0
        self.direita = len(self.matriz[0]) - 1  # subtrai 1 para compensar o índice 0
        self.esquerda = 0
        
        # contadores de linha e coluna, movimentam o "cursor" da matriz
        self.linha = 0
        self.coluna = 0


    # Função que simplifica imprimir o próximo elemento. Se printa o topo ou a direita,
    # o contador aumenta, se printa o fundo ou a esquerda do espiral, o contador reduz.
    # retorna o contador.
    def loop_print(self, direcao: str, contador: int, constante: int, limite: int):
        if direcao == "esquerda" or direcao == "descer":
            while contador < limite:
                if direcao == "esquerda":
                    print(self.matriz[constante][contador])
                else:
                    print(self.matriz[contador][constante])

                contador += 1
        else:
            while contador > limite:
                if direcao == "direita":
                    print(self.matriz[constante][contador])
                else:
                    print(self.matriz[contador][constante])

                contador -= 1
        return contador


    # Verifica se o espiral terminou de ser impresso. 
    # Se a referencia da coluna da esquerda passou a da direita, 
    # ou se a referencia da linha do # topo passou a do fundoa,
    # matriz ja foi impressa completamente.
    # Retorna 1 para verdadeiro, 0 para falso.
    def check(self):
        if self.esquerda > self.direita or self.topo > self.fundo:
            print(self.matriz[self.linha][self.coluna])
            return 1
        return 0

    def printa_espiral(self):
        # !>> Movimento em espiral: desenha topo, depois direita, fundo e a esquerda  <<!
        # Antes de cada nova linha a ser impressa, verifica usando check() se a matriz
        # já foi completamente impressa.
        while True:
            if self.check():
                break
            # printa o topo da matriz
            self.coluna = self.loop_print(direcao="esquerda", contador=self.coluna, 
                                         constante=self.linha, limite=self.direita)
            self.topo += 1  # move controle uma linha pra baixo do topo da matriz

            if self.check():
                break
            # printa a direita da matriz
            self.linha = self.loop_print(direcao="descer", contador=self.linha,
                                      constante=self.coluna, limite=self.fundo)
            self.direita -= 1  # move controle uma linha pra dentro da direita

            if self.check():
                break
            # printa a parte de baixo da matriz
            self.coluna = self.loop_print(direcao="direita", contador=self.coluna,
                                       constante=self.linha, limite=self.esquerda)
            self.fundo -= 1  # move controle uma linha pra cima da parte de baixo

            if self.check():
                break
            # printa a esquerda da matriz
            self.linha = self.loop_print(direcao="subir", contador=self.linha, 
                                      constante=self.coluna, limite=self.topo)
            self.esquerda += 1  # move controle uma linha pra dentro da esquerda


# exemplo01 = [[1, 2, 3, 4],
#              [10, 11, 12, 5],
#              [9, 8, 7, 6]
#             ]
# exemplo02 = [[1, 2],
#              [10, 3],
#              [9, 4],
#              [8, 5],
#              [7, 6]
#             ]
# exemplo03 = [[1, 2, 3, 4, 5],
#              [16, 17, 18, 19, 6],
#              [15, 24, 25, 20, 7],
#              [14, 23, 22, 21, 8],
#              [13, 12, 11, 10, 9]
#             ]
matriz = [[1, 2],
           [8, 3],
           [7, 4],
           [6, 5]
           ]


import sys
# se alguma linha tem um número diferente de colunas do que as outras, a matriz é inválida.
# verifica se a matriz é válida
# começa pelo indice 1, pois a validação subtrai do indice
for linha in range(1, len(matriz)):
    # se tamanho da linha é diferente da linha anterior
    if len(matriz[linha]) != len(matriz[linha - 1]):
        sys.exit("Matriz Inválida")

espiral = Espiral(matriz)
espiral.printa_espiral()
