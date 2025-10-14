# Arquivo (módulo) contabancaria, estou importando
# a classe ContaBancaria
from contabancaria import ContaBancaria
from typing import override

class ContaCorrente(ContaBancaria):
    def __init__(self, numero):
        super().__init__(numero)
        self.limite = 800  # Default

    @override
    def sacar(self, valor):
        if valor <= (self.saldo + self.limite):
            self.saldo -= valor
            return True
        return False 

    @override
    def __str__(self):
        return 'Conta Corrente'