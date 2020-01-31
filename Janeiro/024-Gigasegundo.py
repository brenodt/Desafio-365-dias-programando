"""Exercício 24:
Crie uma função que retorne a data atual mais um gigasegundo.
"""


from datetime import timedelta as td
from datetime import datetime as dt
from time import sleep


def gigasec():
    # 1 gigasegundo = 10^9
    # define variável com a constante
    gigasegundo = 1000000000

    # cria uma instancia de timedelta com
    # um gigasegundo passado como argumento
    # de segundos. Na inicialização, o objeto
    # terá os segundos automaticamente convertidos
    # para dias, segundos e microssegundos
    delta = td(seconds=gigasegundo)

    # toma o momento de agora
    agora = dt.now()
    sleep(10)
    agors = dt.now()

    final = agora + agors
    print(final)
    # retorna agora + um gigasegundo
    return agora + delta


gigasec()
