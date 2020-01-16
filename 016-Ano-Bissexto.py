"""Exercício 16:
Crie uma função que recebe um ano, e que retorna se ele é ou não bissexto.

Um ano é bissexto se:
>> Ele é divisível por 4
    >> Exceto se ele é divisível por 100
        >> A menos que ele também seja divisível por 400.
        
Exemplo: 1997 não é bissexto. 1996 é. 1900 não é bissexto. Mas 2000 é."""


def bissexto(ano: int):
    if ano % 4 == 0:  # se ano é divisível por 4
        if ano % 100 == 0 and ano % 400 != 0:  # se é divisível por 100 e não por 400
            return f"{ano} não é bissexto."

        return f"{ano} é bissexto."

    return f"{ano} não é bissexto."


ano = 2019
print(bissexto(ano))
