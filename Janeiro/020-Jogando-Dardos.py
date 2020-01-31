"""Exercício 20:
Simule um jogo de dardos. Dada uma posição em coordenadas cartesianas, determine quantos pontos o jogador fez.
Fora do alvo: 0 pontos
Circulo exterior (raio = 10): 1 ponto
Circulo do meio (raio = 5): 5 pontos
Centro (raio = 1): 10 pontos
"""


class Dardos():
    def __init__(self):
        self.pontos = 0

    def _aumenta_pontuacao(self, posicao_cartesiana):

        regiao = self._acha_regiao_do_alvo(posicao_cartesiana)

        if regiao == "centro":
            self.pontos += 10
            return 10
        elif regiao == "meio":
            self.pontos += 5
            return 5
        elif regiao == "exterior":
            self.pontos += 1
            return 1
        return 0

    def _acha_regiao_do_alvo(self, posicao_cartesiana: tuple):

        x, y = posicao_cartesiana

        x = abs(x)
        y = abs(y)

        if x >= y:
            if x <= 1:
                return "centro"
            elif x <= 6:
                return "meio"
            elif x <= 16:
                return "exterior"
        else:
            if y <= 1:
                return "centro"
            elif y <= 6:
                return "meio"
            elif y <= 16:
                return "exterior"

    def jogar(self, posicao_cartesiana: tuple):
        ponto = self._aumenta_pontuacao(posicao_cartesiana)
        print(f"""O usuário marcou {ponto} ponto(s) essa rodada.
        Ele está com um total de {self.pontos} ponto(s)!""")


tabuleiro = Dardos()

while True:
    pos = input("Digite a posicao: ")

    if pos == "quit":
        break
    else:
        lst = [int(x) for x in pos.split(" ")]
        pos = tuple(lst)
        tabuleiro.jogar(pos)
