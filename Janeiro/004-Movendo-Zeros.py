"""Exercício: 
Dada uma matriz numérica de uma dimensão, mova todos os zeros presentes para o final, sem alterar a posição relativa dos outros números presentes."""

entrada = [10, 0, 0, 4, 20, 0, 2, 0, 1, 0, 3, 4, 5, 18, 0, 0, 5, 7]
zeros = entrada.count(0)
saida = list(filter(lambda numero: numero > 0, entrada))

for indice in range(zeros):
    saida.append(0)

print(saida)
