"""Exercício 38:
Crie um programa que traduza o valor de um resistor simplificado (que possui apenas dois indicadores)

Preto:    0
Marrom:   1
Vermelho: 2
Laranja:  3
Amarelo:  4
Verde:    5
Azul:     6
Violeta:  7
Cinza:    8
Branco:   9

Não utilize condicionais! (if/else, operador ternário)
"""


def valor_do_resistor(dezena: str, unidade: str):
    # liga o nome da cor com o respectivo valor
    valores = {
        "preto": 0, "marrom": 1, "vermelho": 2,
        "laranja": 3, "amarelo": 4, "verde": 5,
        "azul": 6, "violeta": 7, "cinza": 8,
        "branco": 9
    }
    # normaliza as variáveis
    dezena = dezena.lower()
    unidade = unidade.lower()
    # caso o argumento passado seja inválido retorna erro
    if dezena not in valores.keys() or unidade not in valores.keys():
        return "Cor inválida"
    # o valor da dezena é multiplicado por 10 e somado a unidade
    return valores[dezena] * 10 + valores[unidade]


dez = "branco"
uni = "azul"
print(valor_do_resistor(dez, uni))
