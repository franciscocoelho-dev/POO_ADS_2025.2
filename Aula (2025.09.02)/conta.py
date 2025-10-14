class ContaBancaria:

    #Limitar os atributos da classe
    __slots__ = ['agencia', 'numero', 'titular', '__saldo']

    # Definir o método de inicialização dos objetos
    def __init__(self, agencia, numero, titular):
        self.agencia = agencia
        self.numero = numero
        self.titular = titular
        self.__saldo = 0.00


    def ver_saldo(self):
        return self.__saldo

    def depositar(self, valor):
        if valor > 0:
            self.__saldo += valor  # (self)  saldo = saldo + valor
            return True
        return False
    
    def sacar(self, valor):
        if valor <= self.__saldo:
            self.__saldo -= valor
            return True
        return False



conta1 = ContaBancaria('0011-9', '77333-6', 'Ana Silva')
conta1.saldo = -10000

print(conta1.ver_saldo())

