

def acha_substring(texto: str, substring: str):
    # find() retornará -1 caso a substring não 
    # esteja presente na string "texto"
     if (texto.find(substring) == -1): 
        return false
    # Essa declaração nunca será executada caso
    # a condição acima seja verdadeira. Por isso,
    # não é necessário usar um "else".
    return true
