from random import choice

def quem_ganha(user: str, pc: str):
    # elimina o caso de empate
    if pc == user:
        return "empate"
    else:
        if user == "pedra":
            if pc == "papel":
                return "perdeu"
            else:
                return "ganhou"

        if user == "papel":
            if pc == "tesoura":
                return "perdeu"
            else:
                return "ganhou"

        if user == "tesoura":
            if pc == "pedra":
                return "perdeu"
            else:
                return "ganhou"


"""Simples implementação de Pedra, Papel, Tesoura.
O jogo rodará até o usuário digitar "sair" ou optar por 'nao' em jogar novamente.
A cada rodada, o usuário escolhe uma das três opções,
e pode optar por não jogar novamente respondendo a pergunta com (nao)"""

mensagem_bem_vindo = """Bem vindo ao jogo Pedra, Papel, Tesoura! 
Escolha uma das três opções e jogue contra o computador!
Você pode também digitar "sair" para deixar o jogo. Boa sorte!\n"""

# boas vindas ao usuário
print(mensagem_bem_vindo)

# Array de opções do computador
pc = ["pedra", "papel", "tesoura"]

# Loop rodará até o usuário fechar o jogo
while True:
    # opção aleatória do computador
    pc_rodada_atual = choice(pc)

    # toma a escolha do usuário, usa o método .lower() para normalizar a entrada
    usuario = input("Escolha 'Pedra', 'Papel' ou 'Tesoura': ").lower()

    # verifica se a entrada foi "sair"; se sim, termina
    if usuario == "sair":
        break

    # verifica se o usuário submeteu uma entrada válida
    if usuario != "pedra" and usuario != "papel" and usuario != "tesoura":
        print("\nO que você digitou é inválido! Tente escolher uma das opções a seguir.")
    else:  # se a entrada for válida, roda o senão
        vencedor = quem_ganha(usuario, pc_rodada_atual)

        # printa mensagem de status da rodada
        print(f"Você {vencedor}!")
        # printa no terminal a escolha do computador, do usuário e pergunta se ele quer jogar novamente
        print(f"\nEscolha do computador: {pc_rodada_atual}")
        print(f"Escolha do usuário: {usuario}")
        jogar_novamente = input("Deseja jogar novamente? ").lower()

        # se o input foi não, terminar o jogo
        if jogar_novamente == "nao" or jogar_novamente == "n":
            break
