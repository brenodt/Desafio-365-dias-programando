

# usado para calcular magnitude
from math import hypot

class Vetor():
    # Inicializa a instância, necessário
    # os valores de X e Y
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    # Define o formato de impressão de
    # instâncias da classe: Vetor(x, y)
    def __repr__(self):
        return f'Vetor({self.x}, {self.y})'

    # Configura a saída da função abs()
    # como sendo a magnitude do vetor
    def __abs__(self):
        return hypot(self.x, self.y)

    # Habilita e configura a saída da
    # operação de soma entre instâncias da classe
    def __add__(self, outro_vetor):
        x = self.x + outro_vetor.x
        y = self.y + outro_vetor.y
        return Vetor(x, y)

    # Implementa multiplicação por escalar
    def __mul__(self, escalar: int):
        return Vetor(self.x * escalar, self.y * escalar)
    
