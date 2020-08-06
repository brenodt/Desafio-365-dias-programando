

from collections import deque

def rotaciona(d: deque, n: int):
    # O método rotate considera n > 0 para
    #   rotações 'anti-horárias' (da direita para a esquerda)
    #   e n < 0 para rotações 'horárias' (esqueda para a direita)
    #
    # declaro essa função auxiliar que inverte o sinal só
    # para que a explicação esteja no contexto do exemplo.
    d.rotate(-n)

# Crio um objeto deque (double-ended queue)
dq = deque(range(7))

rotaciona(dq, 3)
print(dq)  # Saída: deque([3, 4, 5, 6, 0, 1, 2])