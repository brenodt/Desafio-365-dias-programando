

def inverte_pontuação(texto: str):

    # Substitui pontos "." por um texto arbitrário
    # Escolhi "akqsr" pois a probabilidade de essa
    # sequência aparecer num texto de verdade é virtualmente
    # inexistente, portanto, não seria substituída errôneamente
    texto = texto.replace('.', 'akqsr')
    texto = texto.replace(',', '.')
    texto = texto.replace('akqsr', ',')
    return texto


texto_teste = 'um, dois. três, quatro.'
print(inverte_pontuação(texto_teste))
