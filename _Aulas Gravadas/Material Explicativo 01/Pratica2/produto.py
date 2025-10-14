from fornecedor import Fornecedor

class Produto:
    def __init__(self, descricao: str, quantidade: float, valor: 'Fornecedor', fornecedor: 'Fornecedor'):
        self.descricao = descricao
        self.quantidade = quantidade
        self.valor = valor
        self.fornecedor = fornecedor


