"""Exercício 12:
Escreva um programa que verifique se uma senha é válida, segundo os seguintes critérios:
1. Pelo menos uma letra minúscula e uma maiúscula [aA-zZ]
2. Pelo menos um número [1-9]
3. Pelo menos um dos três caracteres especiais: [@#$]
4. Tamanho da senha: 6 a 12 caracteres
"""


from string import ascii_lowercase, ascii_uppercase, digits
especiais = "@#$"


def senha_valida(senha: str):
    letra_minuscula = False
    letra_maiuscula = False
    numero = False
    especial = False

    if 6 < len(senha) > 12:
        return "Senha inválida."

    for caractere in senha:
        if caractere in ascii_lowercase and not letra_minuscula:
            letra_minuscula = True
        elif caractere in ascii_uppercase and not letra_maiuscula:
            letra_maiuscula = True
        elif caractere in digits and not numero:
            numero = True
        elif caractere in especiais and not especial:
            especial = True

        if letra_maiuscula and letra_minuscula and numero and especial:
            return "Senha válida."

    return "Senha inválida."
