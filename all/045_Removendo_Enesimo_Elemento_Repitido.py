"""Exercício 45
"""


def remove_enesimo(lista: list, elemento: str, numero: int):
    if numero > lista.count(elemento):
        return "impossible"
    
    contador = 0
    for indice in range(0, len(lista)):
        if lista[indice] == elemento:
            contador += 1
            if contador == numero:
                lista.pop(indice)
                break
    return lista


listaa = ["pó", "pô", "pó"]
num = 2
el = "pó"

print(remove_enesimo(listaa, el, num))
