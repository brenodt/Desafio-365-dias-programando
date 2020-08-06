

# Exemplo onde exec() é usado para executar um texto contendo uma
# declaração de uma função para encontrar o número passado da
# sequência de Fibonacci e printar no terminal
if __name__ == "__main__":

    texto_codigo = """
def fib(numero): 
    if numero < 0:
        return -1
    else:
        if numero == 1 or numero == 2:
            return 1
        else:
            return fib(numero - 1) + fib(numero - 2)

print(fib(7)) 
    """
    exec(texto_codigo)
    ## Saída: 13