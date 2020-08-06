

def palindromo(palavra: str):
    return palavra == palavra[::-1]


if __name__ == "__main__":
    teste = 'banana'
    # Saída: True
    print(palindromo(teste))
