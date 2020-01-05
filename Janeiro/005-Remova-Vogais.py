"""Crie uma função que remova todas as vogais de uma string"""


# Resposta 1: Usando um For Loop e uma comparação com uma lista de vogais
def remove_vogal(texto: str):
    texto = texto.lower()  # normaliza entrada, tranformando texto em letras minúsculas
    vogais = ["a", "e", "i", "o", "u"]  # lista de vogais
    saida = ""  # inicializa variavel

    # itera o texto recebido
    for caractere in texto:
        if not caractere in vogais:  # se a letra não é nenhuma das vogais
            saida += caractere  # adiciona a letra a saida

    return saida


# Resposta 2: Usando a função Filter()
def filtra_vogal(texto: str):
    texto = texto.lower()  # normaliza entrada, tranformando texto em letras minúsculas
    vogais = ["a", "e", "i", "o", "u"]  # lista de vogais
    saida = ""  # inicializa variavel

    # saida é igual a lista resultante do filtro
    saida = list(filter(lambda letra: letra not in vogais, texto))
    # usando o método join() para transformar a lista em texto
    saida = "".join(saida)

    return saida
