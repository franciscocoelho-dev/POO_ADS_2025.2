from contabancaria import *
from typing import override

class ContaPoupanca(ContaBancaria):
    def __init__(self, numero, saldo, dia_rendimento):
        super().__init__(numero, saldo)
        self.dia_rendimento = dia_rendimento

    def inserir_rendimento(self):
        self.saldo += (self.saldo * 0.005)

    @override
    def __str__(self):
        return f'Conta Poupança {self.numero} tem saldo R$ {self.saldo}'
    
