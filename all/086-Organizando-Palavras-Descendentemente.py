

lista_original = [ "Uma", "palavra", "contém", "uma", "ou", "mais", "letras"]
print(id(lista_original), " ; ", lista_original)
# >> 22169040  ;  ['Uma', 'palavra', 'contém', 'uma', 'ou', 'mais', 'letras']

# Atribui a chave a função len, que será usada como parâmetro de organização.
# Usa reverse = True para devolver em ordem descendente.
nova_lista = sorted(lista_original, key=len, reverse=True)

print(id(lista_original), " ; ", lista_original)
# >> 22169040  ;  ['Uma', 'palavra', 'contém', 'uma', 'ou', 'mais', 'letras']
print(id(nova_lista), " ; ", nova_lista)
# >> 22170200  ;  ['palavra', 'contém', 'letras', 'mais', 'Uma', 'uma', 'ou']