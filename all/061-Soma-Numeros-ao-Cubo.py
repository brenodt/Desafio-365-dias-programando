

def soma_elementos_ao_cubo(n: int):
    # Condição de parada da recursão
    if n == 1:
        return 1
    # caso n não seja 1, executa recursão
    return n ** 3 + soma_elementos_ao_cubo(n - 1)


x = 7
print(soma_elementos_ao_cubo(x))
