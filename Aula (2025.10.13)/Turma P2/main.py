from contabancaria import *
from poupanca import *
from contacorrente import *

print('------------------------------------')
conta1 = Poupanca('896-3', 5)
conta1.depositar(200)
print(conta1.saldo)
conta1.gerar_rendimento()
print(conta1.saldo)

print('------------------------------------')
conta2 = ContaCorrente('321-4')
conta2.depositar(200)
conta2.sacar(1400)
print(conta2.saldo)
