# Constante que representa cada botão em uma dada posição de uma lista
TECLADO = [ '1',   'abc2',  'def3',
          'ghi4',  'jkl5',  'mno6',
          'pqrs7', 'tuv8', 'wxyz9',
            '*',   ' 0',    '#'   ]

def cliques(texto):
    # Retorna a soma dos cliques de cada caractere. Python usa índice zero, 
    # então é adicionado um a cada valor de caractere encontrado.
    # É passada a função sum() um objeto gerador que procura, para cada caractere,
    # a posição do caractere em um botão
    # (se o caractere faz parte da string que representa esse botão)
    return sum(1 + botao.find(caractere) for caractere in texto.lower() 
                                      for botao in TECLADO 
                                      if caractere in botao)

# Exemplos
t = "Essa frase tem algumas letras"
print(cliques(t))  # SAÍDA >> 59
t = "CASA"
print(cliques(t))  # SAÍDA >> 9
