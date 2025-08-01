class ContaBancaria:
    def __init__(self, titular, saldo_inicial=0):
        self.__titular = titular
        self.__saldo = saldo_inicial
        
#Método público para depositar      
    def depositar(self, valor):
        if valor >0:
            self.__saldo += valor
            print(f"Depósito de R$ {valor} realizado com sucesso")
        else:
            print(f"Valor de depósito inválido")
#Método público para sacar         
    def sacar(self,valor):
        if 0 < valor <= self.__saldo:
            self.__saldo -= valor
            print(f"Saque de R${valor} realizado com sucesso")
        else:
            print("Saldo insuficiente ou valor inválido para saque")
    
#Método público para consultar saldo
    def consultar_saldo(self):
        return self.__saldo
    
    '''Getter| Setter:
    Getter: é um método usado para obter(ler) o valor de um atributo privado
    de uma classe.
    Setter: é usado para definir(escrever) ou alterar o valor de um atributo
    pribado de uma classe'''

    # getter para o titular (somente leitura)

    @property
    def titular(self):
        return self.__titular

#usar a classe

conta = ContaBancaria("João Silva", 1000) 
print(conta.titular)  #Saída: João Silva
print(conta.consultar_saldo())  #saída: 1000

conta.depositar(500)
print(conta.consultar_saldo())

conta.sacar(200)
print(conta.consultar_saldo)
  
#print(conta.__saldo)   