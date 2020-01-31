"""Exercício 22:
Dada uma idade (em anos inteiros) e um planeta do sistema solar, calcule a idade equivalente neste planeta em segundos e em anos:

Dados:
>> Terra: Ano == 31.557.600 s
>> Mercúrio: Ano == 0.2408467 anos terrestres
>> Vênus: Ano == 0.61519726 anos terrestres
>> Marte: Ano == 1.8808158 anos terrestres
>> Júpiter: Ano == 11.862615 anos terrestres
>> Saturno: Ano == 29.447498 anos terrestres
>> Urano: Ano == 84.016846 anos terrestres
>> Netuno: Ano == 164.79132 anos terrestres
"""


class Solar():
    def __init__(self, idade: int):
        # Guardo a idade da instância
        self.idade = idade
        self.terrestre = self.__terrestre()
        # Dicionário da proporção de anos para cada planeta
        self.planetas = {
            "mercurio": 0.2408467,
            "venus": 0.61519726,
            "marte": 1.8808158,
            "jupiter": 11.862615,
            "saturno": 29.447498,
            "urano": 84.016846,
            "netuno": 164.79132
        }

    def __terrestre(self):  # função privada que converte a idade para segundos
        # o ano tem, na verdade, cerca de 365 dias e 6 horas. Adiciono aqui
        # (((dias) horas + 6) minutos) segundos
        return (((self.idade * 365) * 24 + 6) * 60) * 60

    def __converte_planeta(self, planeta: str):
        # o resultado é a idade, em segundos do parâmetro planeta
        return self.terrestre * self.planetas[planeta]

    # retorna o equivalente em anos terrestres
    def __em_anos_terrestres(self, segundos: float):
        return (((segundos / 60) / 60) / 24 - 6) / 365

    def converte(self, planeta: str):
        # usando formatação para reduzir o número de casas decimais
        # retorna uma string, então no caso de segundos, que são usados em cálculo, retorno para float
        segundos = float("{0:.2f}".format(self.__converte_planeta(planeta)))
        anos = "{0:.2f}".format(self.__em_anos_terrestres(segundos))
        return f"No planeta {planeta}, você tem {segundos} segundos de idade, o equivalente a cerca de {anos} anos terrestres."


eu = Solar(18)
print(eu.terrestre)
var = eu.converte("marte")
print(var)
