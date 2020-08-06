


def Filtra_Tupla(lista):
    # Serão adicionadas à saída tuplas cujo valor
    # não seja vazio.
    saida = [tupla for tupla in lista if tupla]
    return saida 
  

tuplas = [(), (0, "ABC", 24), (), (1, "BCD", 46),  
          (2, "CDE", 70), (3, "DEF", 13), ()]
print(Filtra_Tupla(tuplas))
# SAIDA:
# >> [(0, 'ABC', 24), (1, 'BCD', 46), (2, 'CDE', 70), (3, 'DEF', 13)]