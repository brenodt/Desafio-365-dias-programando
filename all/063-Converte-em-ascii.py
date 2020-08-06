

def retorna_ascii(caractere):
    # retorna uma string formatada contendo o char e o código ASCII dele
    return f'O caractere "{caractere}" é representado pelo código {ord(caractere)}'


char = "@"
ascii = retorna_ascii(char)
print(ascii)
# -- OUTPUT --
# O caractere "@" é representado pelo código 64
