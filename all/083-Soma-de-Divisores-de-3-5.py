'''
If we list all the natural numeros below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. 
The soma of these multiples is 23.

Finish the solution so that it returns the soma of all the multiples of 3 or 5 below the numero passed in.

Note: If the numero is a multiple of both 3 and 5, only count it once.
'''

def solucao(numeros):
    soma = 0
    for numero in range(numeros):
        if numero % 3 == 0 or numero % 5 == 0:
            soma += numero
    return soma