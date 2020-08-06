'''
Módulo de Conversão de base

As funções do módulo seguem a convenção de nome: baseX_baseY()
onde:
        · x = base de origem
        · y = base procurada

Funções cuja origem é decimal recebem argumentos de tipo int()
As demais recebem argumentos de tipo str()

Motivo: facilidade de manipulação.
    O método para converter DE base10 PARA (Y) consiste em divisões sucessivas.
        >> Portanto, o parâmetro precisa ser um número
    O método para converter DE (Y) PARA base10 consiste em manipular os dígitos de trás pra frente.
        >> Portanto, o parâmetro deve ser um str(), para que ele seja invertido e fracionado
'''

def parcela(iteravel, tamanho_da_fatia):
    '''
Função Auxiliar que retorna `iteravel` dividido em n partes de tamanho igual a `tamanho_da_fatia`
    '''
    for indice in range(0, len(iteravel), tamanho_da_fatia):
        yield iteravel[indice:indice + tamanho_da_fatia]


HEXADECIMAL = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']

def base10_baseX(decimal: int, base: int):
    x = ''
    while True:
        if decimal < base:
            if base == 16:
                return ( x + HEXADECIMAL[decimal] )[::-1]
            return (x + str(decimal))[::-1]
        
        if base == 16:
            novo_numero = decimal % base
            x += HEXADECIMAL[novo_numero]  # converte cada dígito para o equivalente na base 16
        else:
            x += str(decimal % base)
        decimal = decimal // base

def baseX_base10(numero: str, base: int):
    if base == 16:
        numero = [ HEXADECIMAL.index(x) for x in numero.upper()[::-1] ]  # Converte cada dígito para o equivalente na base 10
    else:
        numero = numero[::-1]
    return sum( [ int(x[0]) * (2 ** x[1]) for x in zip(numero, range(len(numero))) ] )


#
#   Base 10 >> Base 2
#   Base 10 << Base 2
#
def base10_base2(decimal: int):
    x = ''
    while True:
        if decimal < 2:
            return (x + str(decimal))[::-1]
        
        x += str(decimal % 2)
        decimal = decimal // 2

def base2_base10(binario: str):
    binario = binario[::-1]
    return sum( [ int(x[0]) * (2 ** x[1]) for x in zip(binario, range(len(binario))) ] )

#
#   Base 10 >> Base 8
#   Base 10 << Base 8
#
def base10_base8(decimal: int):
    x = ''
    while True:
        if decimal < 8:
            return (x + str(decimal))[::-1]
        
        x += str(decimal % 8)
        decimal = decimal // 8

def base8_base10(octal: str):
    octal = octal[::-1]
    return sum([ int(x[0]) * (8 ** x[1]) for x in zip(octal, range(len(octal))) ] )

#
#   Base 10 >> Base 16
#   Base 10 << Base 16
#
def base10_base16(decimal: int):
    x = ''
    while True:
        if decimal < 16:
            return ( x + HEXADECIMAL[decimal] )[::-1]
        
        novo_numero = decimal % 16
        decimal = decimal // 16

        x += HEXADECIMAL[novo_numero]

def base16_base10(hexadecimal: str):
    hexadecimal = [ HEXADECIMAL.index(x) for x in hexadecimal.upper()[::-1] ]
    return sum([ int(x[0]) * (16 ** x[1]) for x in zip(hexadecimal, range(len(hexadecimal))) ])

#
#   Base 2 >> Base 16
#   Base 2 >> Base 8
#   Base 2 << Base 8
#
def base2_base16(binario: str):
    binario_invertido = list(parcela(binario[::-1], 4))
    decimal = [ HEXADECIMAL[ base2_base10(x[::-1]) ] for x in binario_invertido ][::-1]
    return ''.join(decimal)

def base2_base8(binario: str):
    binario_invertido = list(parcela(binario[::-1], 3))
    decimal = [ str( base2_base10(x[::-1]) ) for x in binario_invertido ][::-1]
    return ''.join(decimal)

def base8_base2(octal: str):
    binario = ''
    for digito in octal:
        n = base10_base2( int(digito) )
        while len(n) < 3:
            n = '0' + n

        binario += n
    return binario
    
if __name__ == "__main__":
    # numero = 622
    numero = '5331'

    # print(base10_base2(numero))
    # print(base2_base10(numero))

    # print(base10_base8(numero))
    # print(base8_base10(numero))

    # print(base10_base16(numero))
    # print(base16_base10(numero))

    # print(base2_base16(numero))
    # print(base2_base8(numero))

    print(base8_base2(numero))
