from produto import Produto
from fornecedor import Fornecedor

f1 = Fornecedor('Material Brasil Ltda.', 'contato@materialbrasil.com.br', '8633669977')
p1 = Produto('Caneta', 50, 3.50, f1)

print(p1.fornecedor)

