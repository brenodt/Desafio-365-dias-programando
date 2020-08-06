

class Classe():
    def __init__(self, alunos: dict):
        self._alunos = alunos

    def __getitem__(self, pos):
        notas = self._alunos[pos]
        total = 0
        for nota in notas:
            total += nota
        return total / len(notas)

if __name__ == "__main__":
    
    dicionario = {
        "Andre": [0, 10, 5, 2],
        "Sandra": [10, 6, 7],
        "Tobias": [8, 4, 1, 2],
        "George": [10, 9, 8, 7]
        }
    classe = Classe(dicionario)
    media = classe["Andre"]
    print(media)
