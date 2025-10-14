from contapoupanca import *

cp1 = ContaPoupanca('0014-9', 100, 5)
print(cp1.saldo)
cp1.inserir_rendimento()
print(cp1.saldo)


