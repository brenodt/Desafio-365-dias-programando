


def converte_formato_hora(hora: str):
    # Classifica em AM ou PM
    if hora[-2:] == "AM":
        # se 12, retorna 00:[minutos]
        if hora[:2] == "12":
            return "00" + hora[2:-3]
        # senão, retorna a hora menos AM
        else:
            return hora[:-3]
    elif hora [-2:] == "PM":
        # se 12m retorna a hora menos PM
        if hora[:2] == "12":
            return hora[:-3]
        # senão, retorna a [hora mais 12]:[minutos]
        else:
            return str(int(hora[:2]) + 12) + hora[2:-3]


h = "10:17 PM"
print(converte_formato_hora(h))
