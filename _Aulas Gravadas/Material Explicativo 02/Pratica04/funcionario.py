from endereco import Endereco

class Funcionario:
    # Método de Inicialização
    def __init__(self, nome, email):
        self.nome = nome
        self.email = email
        self.endereco = None
    
    def __str__(self):
        return self.nome
    
    def adicionar_endereco(self, logradouro, numero, bairro):
        self.endereco = Endereco(logradouro, numero, bairro)
    
    
    def __del__(self):
        print(f'Foi removido da memória o funcionário {self.nome}')

