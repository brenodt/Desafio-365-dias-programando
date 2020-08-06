"""Exercício 43:

crie uma função alarme que toca um alarme após N segundos.
"""


import datetime as dt
from winsound import Beep


def beep_n_vezes(n: int):
    # loop não utiliza a variável
    # apenas repete a função Beep
    # um número N de vezes
    for vez in range(0, n):
        Beep(500, 200)

def alarme(segundos: int, beeps: int):
    # objetos timedelta permitem operações
    # aritméticas com objetos datetime
    delta = dt.timedelta(seconds=segundos)
    # o tempo final é o atual mais o argumento
    t_final = dt.datetime.now() + delta

    while True:
        # compara o tempo atual com o final
        if dt.datetime.now() >= t_final:
            beep_n_vezes(beeps)
            return


print(alarme(5))

