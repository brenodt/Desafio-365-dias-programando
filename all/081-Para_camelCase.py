def para_camel_case(texto):
    # Separa o texto em palavras, usando operador ternário para
    # diferenciar os dois tipos possíveis de separadores
    palavras = texto.split("-") if "-" in texto else texto.split("_")
    saida = []  # inicializa sa´da
    for indice in range(len(palavras)):
        palavra = palavras[indice]  # Armazena a palavra
        if indice == 0:  # Caso seja a primeira palavra
            saida.append(palavra[0].lower() + palavra[1:])
        else:  # Demais palavras
            saida.append(palavra[0].upper() + palavra[1:])
    return "".join(saida)


t = 'the_stealth_warrior'
print(para_camel_case(t))
t = 'The-Stealth-Warrior'
print(para_camel_case(t))
t = 'A-B-C'
print(para_camel_case(t))
