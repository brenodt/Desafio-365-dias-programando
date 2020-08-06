

lista = ["Essa", "lista", "representa",
         "um", "conjunto", "qualquer",
         "de", "elementos", ":-)"
        ]
n = 3

# Utiliza yield para retomar a posição da função
# a cada execução.    
def parcela_lista(lista, elementos_por_parcela):
    # Utiliza o parâmetro "passo" da função range para evitar
    # repetição de elementos
    for indice in range(0, len(lista), elementos_por_parcela):
        # Retorna a parcela referente a execução usando fatiamento
        yield lista[indice:indice + elementos_por_parcela]


# O resultado é um objeto gerador. 
# Passo pelo construtor list para gerar uma lista com o resultado da função
lista_parcelada = list(parcela_lista(lista, n))
print(lista_parcelada)
#                                         << Saída >> 
# [['Essa', 'lista', 'representa'], ['um', 'conjunto', 'qualquer'], ['de', 'elementos', ':-)']]
