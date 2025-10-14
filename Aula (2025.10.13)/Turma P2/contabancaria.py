from abc import ABC, abstractmethod

class ContaBancaria(ABC):

    # Método de Inicialização
    def __init__(self, numero):
        self.numero = numero
        self.saldo = 0 # default
    
    def sacar(self, valor):
        if valor <= self.saldo:
            self.saldo -= valor
            return True
        return False

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            return True
        return False

    @abstractmethod
    def __str__(self):
        pass

    