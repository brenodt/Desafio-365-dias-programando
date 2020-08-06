

def filtra_lista(lista: list):
    # Considerando que um número pode ser uma instância de um int ou de um float
    # bool pode ser considerado como 0 ou 1, e portanto é avaliado com instância de int. 
    # Por esse motivo, elimino a opção utilizando um condicional a mais.
    return [elem for elem in lista 
            if (isinstance(elem, int) and not isinstance(elem, bool)) or isinstance(elem, float)]


if __name__ == "__main__":
    teste = ['abc', True, {"A": 123}, 123, 123.123, (123, 'abc'), [456, 'def'], 456, 456.456]
    print(filtra_lista(teste))
    # SAÍDA:
    # >> [123, 123.123, 456, 456.456]
