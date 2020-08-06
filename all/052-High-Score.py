
class Leaderboard():
    def __init__(self):
        self.scores = []  # inicializa tabela de pontuação
        self.sorted_scores = []  # inicializa tabela organizada

    # Adiciona uma nova tuple a tabela.
    # --! USE O FORMATO: (pontuação, nome_do_jogador) !--
    #
    # A última entrada estará sempre a última posição
    # da lista.
    def adiciona_pontuacao(self, entrada: tuple):
        self.scores.append(entrada)
        self.sorted_scores.append(entrada)
        self.__organiza_leaderboard()

    # Método privado utilizado para organizar em ordem
    # decrescente as pontuações
    def __organiza_leaderboard(self):
        return self.sorted_scores.sort(key=lambda par: par[0], reverse=True)

    # Retorna o jogador com a maior pontuação na tabela
    def primeiro_lugar(self):
        return self.sorted_scores[0]

    # Retorna os três primeiros com maior pontuação
    def tres_primeiros(self):
        return self.sorted_scores[0], self.sorted_scores[1], self.sorted_scores[2]

    # Retorna o último jogador adicionado
    def ultimo_jogador_adicionado(self):
        return self.scores[-1]

"""----- OUTPUT -----
Primeiro Colocado: KEW, 700 pontos.

-------------------------------------------------------
Primeiro Colocado: KEW, 700 pontos.
Segundo  Colocado: ASD, 500 pontos.
Terceiro Colocado: AAA, 100 pontos.

-------------------------------------------------------
Último Jogador Adicionado: NEW, 10 pontos.
"""
if __name__ == "__main__":
    
    pontos = Leaderboard()

    pontos.adiciona_pontuacao((100, "AAA"))
    pontos.adiciona_pontuacao((500, "ASD"))
    pontos.adiciona_pontuacao((700, "KEW"))
    pontos.adiciona_pontuacao((10, "NEW"))

    primeiro = pontos.primeiro_lugar()
    tres = pontos.tres_primeiros()
    ultimo_adicionado = pontos.ultimo_jogador_adicionado()
    
    print(f"Primeiro Colocado: {primeiro[1]}, {primeiro[0]} pontos.")
    print("\n-------------------------------------------------------")
    print(f"""Primeiro Colocado: {tres[0][1]}, {tres[0][0]} pontos.
Segundo  Colocado: {tres[1][1]}, {tres[1][0]} pontos.
Terceiro Colocado: {tres[2][1]}, {tres[2][0]} pontos.""")
    print("\n-------------------------------------------------------")
    print(f"Último Jogador Adicionado: {ultimo_adicionado[1]}, {ultimo_adicionado[0]} pontos.")
    