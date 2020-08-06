

# inicializa lista com elementos a serem indexados
lista = ['A', 'B', 'C', 'D', 'F', 'G']

# enumarate() recebe uma sequência e retorna um
# iterável contendo um par igual a (índice, elemento)
# para cada elemento da sequência original
nova_lista = list(enumerate(lista))

#                    ---- OUTPUT ----
# [(0, 'A'), (1, 'B'), (2, 'C'), (3, 'D'), (4, 'F'), (5, 'G')]
print(nova_lista)
