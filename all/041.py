
def multp(iteravel):
    resultado = 1
    for numero in iteravel:
        resultado *= numero
    return resultado

def elemento_n(lista: list, posicao: int):
    return multp([sub_tuple[posicao] for sub_tuple in lista])
