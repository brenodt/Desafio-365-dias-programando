

# Função que retorna uma lista preenchida por um elemento
# n: um número (ou string contendo número) natural
# v: valor a ser usado para preencher a lista
def preenche(n, v):
    # Uso o bloco try-except para levantar o tipo de
    # erro definido por mim, caso n não seja uma string 
    # válida para conversão de str() para int().
    try:
        n = int(n)
    except:
        raise TypeError('%s não é um argumento válido.' % (n,))
    else:
        # else só será executado se a cláusula try não
        # levantar uma exceção
        if n >= 0:  # caso n seja maior ou igual a zero
            # retorne uma lista contendo n elementos v
            return [el for i in range(n)
                       for el in [v]]
        # se n for menor que zero, também levanta um TypeError
        raise TypeError('%s não é um argumento válido.' % (n,))