#Função X Classe
#Função: bloco de código que executa uma tarefa
#Classe: modelo para criar objetos 
#Objeto: É uma estrutura que representa uma  entidade do mundo real ou conceito abstrato de um programa
class ContaBancaria:
    def _init_(self, titular, saldo_inicial= 0):
        #Quando utlizar _init_: quando precisa inicializar o objeto com algum valor ou configuração
        self.titular = titular  #instância atual do objeto
        self.saldo = saldo_inicial 

        

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor   #self.saldo= self.saldo + valor
            print(f"Depósito de R$ {valor:.2f}")
        else:
            print(f"Valor de depósito inválido!")
    
    #criar funções sacar e consultar_saldo
    def saque(self, saque):
        if 0 < saque <= self.saldo:
            self.saldo -= saque
            print(f"Saque de R$ {saque:.2f} realizado com sucesso!")
        else:
            print(f"Saldo insuficiente ou valor inválido")

    def consultar_saldo(self):
        print(f"Saldo atual: R${self.saldo: .2f}")


conta = ContaBancaria("Anna Luiza", 1000)
conta.consultar_saldo()
conta.depositar(500)
conta.sacar(200)
conta.consultar_saldo()
       

           
       