class ContaBancaria:

    # Limitar os atributos
    __slots__ = ['agencia', 'numero', 'titular', '__saldo']

    # Método Inicializador
    def __init__(self, agencia, numero, titular):
        self.agencia = agencia
        self.numero = numero
        self.titular = titular
        self.__saldo = 0.0  # Atributo Privado

    def depositar(self, valor):
        if valor > 0:
            self.__saldo += valor  # (self) saldo = saldo + valor
            return True
        return False
    
    def sacar(self, valor):
        if self.__saldo >= valor:
            self.__saldo -= valor
            return True
        return False

    def consultar_saldo(self):
        return self.__saldo



conta1 = ContaBancaria('0023-x', '33355-2', 'Ana da Silva')
# conta1.saldo = -10000


# print(conta1.saldo)







