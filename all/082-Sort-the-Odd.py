'''
You have an array of numbers.
Your task is to sort ascending odd numbers but even numbers must be on their places.

Zero isn't an odd number and you don't need to move it. If you have an empty array, you need to return it.
'''

def organiza_impares(referencia):
    # Separa ímpares da entrada
    impares = [x for x in referencia if x % 2 != 0]
    impares.sort()  # Organiza ímpares em ordem crescente
    
    # Substitui na entrada ímpares por um marcador de posição qualquer,
    # no caso, "A"
    placeholder = ["A" if x % 2 != 0 else x for x in referencia]

    for impar in impares: # Para cada ímpar
        # substituir o próximo marcador "A" pelo ímpar
        placeholder[placeholder.index("A")] = impar
    return placeholder  # retorna a lista corrigida