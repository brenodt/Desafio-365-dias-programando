'''
Bob is preparing to pass IQ test. The most frequent task in this test is to find out which one of the given numbers differs from the others. Bob observed that one number usually differs from the others in evenness. Help Bob — to check his answers, he needs a program that among the given numbers finds one that is different in evenness, and return a position of this number.

! Keep in mind that your task is to help Bob solve a real IQ test, which means indexes of the elements start from 1 (not 0)

##Examples :

iq_test("2 4 7 8 10") => 3 // Third number is odd, while the rest of the numbers are even

iq_test("1 2 1 1") => 2 // Second number is even, while the rest of the numbers are odd
'''

def iq_test(numbers):
    remainder = [int(i) % 2 for i in numbers.split(" ")]
    return remainder.index(1) + 1 if remainder.count(1) is 1 else remainder.index(0) + 1


def achando_outlier(numeros: str):
    numeros_separados = numeros.split(" ")
    restos = [int(numero) % 2 for numero in numeros_separados]
    return numeros_separados[restos.index(1)] if restos.count(1) is 1 else numeros_separados[restos.index(0)]


n = "2 3 12 14 16 4 6 10"
print(achando_outlier(n))
