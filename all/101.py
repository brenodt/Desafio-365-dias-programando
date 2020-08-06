

def dupl(texto1, texto2):
    duplicados = [elemento for elemento in set(texto1) if elemento in set(texto2)]

    return len(duplicados), duplicados


t1 = 'aabcddekll12@'
t2 = 'bb2211@55k'

print(dupl(t1, t2))