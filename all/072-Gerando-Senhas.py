# Importando Sequências contendo caracteres para seleção aleatória
from string import ascii_letters  # Importa as letras (maiúsculas e minúsculas)
from string import punctuation  # Esses são os símbolos a serem usados
from string import digits  # Por fim, importa os números
# Essa função será usada como base de toda a geração da senha
from random import choice

# Recebe três variáveis que determinam quantos caracteres
# de cada categoria a senha criada terá.
def gerar_senha(letras: int, numeros: int, simbolos: int):
    if abs(letras) + abs(numeros) + abs(simbolos) < 6:  # tamanho mínimo
        return
    # Inicialmente, as opções de caracteres são 3, definidas acima
    opcao = [['letras', letras], ['numeros', numeros], ['simbolos', simbolos]]
    senha = ''  # Inicializa senha
    while True:
        proximo_tipo = choice(opcao)  # Escolhe o próximo tipo de caractere
        
        if proximo_tipo[1] <= 0:  # Caso não tenham mais a serem adicionadas
            opcao.remove(proximo_tipo)  # Remove essa opção da lista
        else:  # Avalia cada opção
            if proximo_tipo[0] == 'letras':
                caractere = choice(ascii_letters)  # Escolhe letra
            elif proximo_tipo[0] == 'numeros':
                caractere = choice(digits)  # Escolhe dígito
            elif proximo_tipo[0] == 'simbolos':
                caractere = choice(punctuation)  # Escolhe símbolo
            
            proximo_tipo[1] -= 1  # Decrementa o contador que foi escolhido
            senha += caractere  # Adiciona o novo caractere na senha
        if len(opcao) == 0:  # Condição de parada
            return senha


if __name__ == "__main__":
    letters = -10
    numbers = 6
    simbols = -1
    print(gerar_senha(letters, numbers, simbols))
