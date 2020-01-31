"""Exercício 23:
Simule o gerenciamento de um banco. Crie as funções:

>> Abrir conta
>> Depositar
>> Sacar
>> Transferir
>> Fechar
"""

from random import randrange


class Banco():
    # Estes são atributos de Controle!
    # Como quero que cada instância criada compartilhe desses atributos,
    # não os coloco dentro de um __init__. Assim, cada instância acessa
    # as variáveis, ao invés de cada uma ter acesso somente ao seu atributo
    contas = {}
    estado_da_conta = {}
    saldo = {}

    def criar_conta(self, nome_da_pessoa):
        # chama método privado para gerar numero de conta
        numero = self.__gerar_número_de_conta()
        # cria par chave:valor no dicionário de contas
        self.contas[numero] = nome_da_pessoa
        # atualiza o estado da conta para aberto
        self.estado_da_conta[numero] = "aberto"
        print(f"conta {numero} aberta.")
        return numero  # se bem sucedido, retorna o numero da conta aberta

    # muda o estado da conta
    def fechar_conta(self, numero_da_conta):
        self.estado_da_conta[numero_da_conta] = "fechado"
        print(f"conta {numero_da_conta} fechada.")

    # retorna se a conta está aberta ou não
    def status(self, numero_da_conta):
        return self.estado_da_conta[numero_da_conta]

    # método privado que gera o número de conta aleatoriamente.
    # possui uma falha de lógica pois só permite a criação de 10.000 contas,
    # quando todas já tiverem sido geradas, estará preso em um loop infinito
    # mas funciona pra provar o conceito
    def __gerar_número_de_conta(self):
        numero = ""
        while True:
            while len(numero) < 4:
                numero += str(randrange(0, 9, 1))
            # verifica se já existe conta com o número criado, senão cria outro
            if numero not in self.contas.keys():
                return numero


class Conta(Banco):  # sub-classe do banco, herda os atributos e métodos
    def __init__(self, nome_da_pessoa):
        self.conta = self.criar_conta(nome_da_pessoa)
        self.titular = nome_da_pessoa
        self.saldo[self.conta] = 0
        self.extrato = 0

    # muda o montante no dicionário de saldo e na instância
    def depositar(self, montante: float):
        if self.status(self.conta) == "aberto":  # verifica estado da conta
            self.saldo[self.conta] += montante
            self.extrato += montante
        else:
            print("A conta está fechada.")

    def sacar(self, montante: float):
        if self.status(self.conta) == "aberto":  # verifica estado da conta
            if montante > self.saldo[self.conta]:  # verifica se há o montante no saldo
                aprovacao = input("Você ficará negativo. Proceder? (Y/N): ").lower()
                if aprovacao == "n":
                    return 0
            self.saldo[self.conta] -= montante
            self.extrato -= montante
            return 1
        else:
            print("A conta está fechada.")

    def transferir(self, montante: float, conta_a_receber):
        # verifica se a conta a receber existe no "banco de dados"
        if conta_a_receber.conta in self.contas.keys():
            # verifica estado da conta
            if self.estado_da_conta[conta_a_receber.conta] == "aberto":  
                if montante > self.saldo[self.conta]:  # verifica se há o montante no saldo
                    aprovacao = input("Você ficará negativo. Proceder? (Y/N): ").lower()
                    if aprovacao == "n":
                        return 0
                    self.saldo[conta_a_receber.conta] += montante
                    conta_a_receber.extrato += montante

                    self.saldo[self.conta] -= montante
                    self.extrato -= montante
                    return 1
            else:
                print("A conta está fechada.")
        else:
            print("Conta a receber inexistente.")


conta1 = Conta("Breno Teodoro")
conta2 = Conta("Natali Baldoni")

conta1.depositar(500.45)
conta1.transferir(300.10, conta2)
conta2.transferir(10.05, conta1)
conta1.sacar(400)
conta2.fechar_conta(conta2.conta)

conta1.transferir(10, conta2)
conta2.sacar(10)
