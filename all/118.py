

def numeros_primos(inicio: int, fim: int):
    # Condições de exclusão para intervalos inválidos
    if inicio <= fim and inicio > 1 and fim > 1:
        saída = []  # Inicializa lista de saída
        for número in range(inicio, fim):
            # Para cada iteração, pressupõe que o número é primo
            primo = True
            # Loop interno, usado para testar cada divisor possível
            for divisor in range(2, int(número ** 0.5) + 1):
                if número % divisor == 0:  # Se é divisível
                    primo = False  # O número é composto
                    break  # pára o loop, já não precisamos continuar
            if primo:  # Caso seja primo
                saída.append(número)  # adiciona ao final da lista
        return saída
    # Caso o intervalo seja inválido, gera um erro de valor
    raise ValueError('Intervalo invalido')

if __name__ == "__main__":
    print(numeros_primos(2, 24))
