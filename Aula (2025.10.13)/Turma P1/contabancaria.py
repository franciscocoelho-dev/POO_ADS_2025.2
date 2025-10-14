from abc import ABC, abstractmethod

class ContaBancaria(ABC):

    # Método de Inicialização
    def __init__(self, numero, saldo):
        self.numero = numero
        self.saldo = saldo
  
    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
    
    def sacar(self, valor):
        if valor <= self.saldo:
            self.saldo -= valor
            return True
        return False
    
    @abstractmethod
    def __str__(self):
        raise NotImplementedError
    
