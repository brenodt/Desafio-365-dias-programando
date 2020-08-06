

def achando_vogais(texto):
    vogais = set("aeiou")
    contador = 0

    for letra in texto:
        if letra.lower() in vogais:
            contador += 1
    
    return f"Número de vogais: " + str(contador)


t = "Texto base com vogais."
print(achando_vogais(t))
## >> Número de vogais: 8
