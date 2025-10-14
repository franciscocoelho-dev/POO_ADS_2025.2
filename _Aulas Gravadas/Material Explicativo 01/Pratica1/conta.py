class ContaBancaria:

    # Método de inicialização
    def __init__(self, numero: str, titular: str):
        self.__numero = numero
        self.__titular = titular
        self.__saldo = 0.0

    def ver_saldo(self) -> float:
        return self.__saldo
    
    def depositar(self, valor) -> bool:
        if valor > 0:
            self.__saldo += valor
            return True
        return False
    
    def sacar(self, valor) -> bool:
        if self.__saldo >= valor:
            self.__saldo -= valor
            return True
        return False
    
    def transferir(self, valor: float, conta_destino: 'ContaBancaria'):
        if self.sacar(valor) == True:
            conta_destino.depositar(valor)
            return True
        return False



conta1 = ContaBancaria('0011-2', 'Maria da Silva')
conta1.depositar(1000)

conta2 = ContaBancaria('08877-6', 'Mário de Oliveira')
conta2.depositar(300)

conta1.transferir(1250, conta2)

print(f'O saldo da Conta1 é: R$ {conta1.ver_saldo()}')
print(f'O saldo da Conta2 é: R$ {conta2.ver_saldo()}')



