"""Exercício 9:
Crie duas funções que façam a conversão de números decimais para binário, e de binário para decimal, sem usar funções 'built-in'"""


def converte_para_decimal(binario: int):
    # converte para string pra acessar cada dígito separado
    binario_str = str(binario)
    # inverte a string, pra começar da direita pra esquerda
    binario_str = binario_str[::-1]

    potencia = 0  # cada dígito do valor binario representa o valor de uma potencia de 2, começando de 2 elevado a zero

    # inicializa o valor decimal
    decimal = 0
    for digito in binario_str:
        # começa o loop convertendo o dígito de volta pra int
        digito = int(digito)
        # o decimal é incrementado da multiplicação do dígito pela potência de 2
        decimal += digito * (2 ** potencia)
        potencia += 1  # incrementa o contador da potência

    return decimal


def converte_para_binario(decimal: int):
    # o valor binário será armazenado numa str
    binario = ""
    # inicializa a variável do quociente com o número decimal que foi passado
    quociente = decimal
    while True:
        # se o quociente é maior que um, adiciona o resto da divisão no valor binário
        resto = quociente % 2
        quociente = quociente // 2  # diminui o quociente
        binario += str(resto)
        # se o quociente é menor ou igual a um, adiciona ele no valor binário
        if quociente <= 1:
            binario += str(quociente)
            # lê-se o valor binário de trás para frente
            binario = int(binario[::-1])
            return binario
