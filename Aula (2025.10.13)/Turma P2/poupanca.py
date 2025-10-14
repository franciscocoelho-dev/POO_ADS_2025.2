# Arquivo (módulo) contabancaria, estou importando
# a classe ContaBancaria
from contabancaria import ContaBancaria
from typing import override

class Poupanca(ContaBancaria):
    def __init__(self, numero, aniversario):
        super().__init__(numero)
        self.aniversario = aniversario

    def gerar_rendimento(self):
        self.saldo += (self.saldo * 0.005)

    @override
    def __str__(self):
        return 'Conta Poupança'

