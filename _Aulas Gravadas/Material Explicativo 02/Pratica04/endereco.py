class Endereco:
    def __init__(self, logradouro, numero, bairro):
        self.logradouro = logradouro
        self.numero = numero
        self.bairro = bairro
    
    def __str__(self):
        return f'{self.logradouro}, {self.numero}. {self.bairro}'
    
    def __del__(self):
        print(f'Foi removido da memória o endereco {self.logradouro}, {self.numero}')
