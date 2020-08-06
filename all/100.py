


import re  # Importa o módulo "regular expressions"
  
def acha_url(texto): 
    # Utiliza a função findall() do módulo re
    # para encontrar todas as ocorrências não
    # sobrepostas de uma RegEx a ser utilizada.
    #
    # A expressão regular é aplicada em um argumento
    # "texto", e o resultado é uma lista contendo as
    # ocorrências da expressão. Nesse caso, uso uma
    # expressão regular para encontrar uma URL qualquer.
    urls = re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', texto) 
    return urls
      
# Código teste 
texto = '''Meu instagram:
https://www.instagram.com/devdiario/
A bíblia dos programadores:
https://stackoverflow.com/
'''
print("Urls: ", acha_url(texto)) 
# Saída: 
# Urls:  ['https://www.instagram.com/devdiario/', 'https://stackoverflow.com/']