
# Vou usar o valor infinito pra garantir que o primeiro
# elemento seja adicionado, pois, independente da
# formatação da lista, o último elemento deve ser considerado
# como maior que todos à sua direita
from math import inf as infinito

def maiores_elementos_a_direita(lista: list):
    maior_valor = -infinito  # Referência do maior valor
    saida = []  # inicializa lista da saída

    # Começando do último índice para o primeiro.
    # Fazemos a verificação contrária da lista
    for i in range(len(lista) - 1, -1, -1):
        # Se o elemento é maior que a referência
        if lista[i] > maior_valor:
            maior_valor = lista[i]  # Atualiza referência
            saida.append(lista[i])  # Adiciona valor na saída

    return saida[::-1]  # retorna o valor invertido


if __name__ == "__main__":
    #l = [10, 1, 9, 2, 8, 7, 1, 2]
    l = []
    print(maiores_elementos_a_direita(l))
