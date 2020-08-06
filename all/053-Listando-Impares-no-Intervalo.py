

def impares_no_intervalo(intervalo: tuple, lista: list):
    inicial, final = intervalo
    return [numero for numero in lista if numero % 2 != 0 and inicial <= numero <= final]


limite = (0,10)
l = [-2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

# --- OUTPUT ---
# [1, 3, 5, 7, 9]
print(impares_no_intervalo(limite, l))
