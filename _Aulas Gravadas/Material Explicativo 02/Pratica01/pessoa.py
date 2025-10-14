class Pessoa:

    # Atributo / Variável da Classe Pessoa, e não dos objetos criados
    quant_pessoas = 0

    def __init__(self, nome, email):
        self.nome = nome
        self.email = email
        Pessoa.quant_pessoas += 1

    def __str__(self):
        return f'{self.nome} - {self.email}'

    @classmethod
    def quantidade_pessoas(cls):
        return cls.quant_pessoas


pessoa1 = Pessoa('Maria', 'maria@gmail.com')
pessoa2 = Pessoa('João', 'joao@gmail.com')
pessoa3 = Pessoa('Ana', 'ana@gmail.com')

print(f'Quant. de Pessoas criadas: {Pessoa.quantidade_pessoas()}')

