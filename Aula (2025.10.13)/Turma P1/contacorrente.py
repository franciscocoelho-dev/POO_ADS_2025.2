from typing import override
from contabancaria import *

class ContaCorrente(ContaBancaria):
    
    def __init__(self, numero, saldo):
        super().__init__(numero, saldo)
        self.cheque_especial = 800  # default
    
    @override
    def sacar(self, valor):
        if valor <= (self.saldo + self.cheque_especial):
            self.saldo -= valor
            return True
        return False
