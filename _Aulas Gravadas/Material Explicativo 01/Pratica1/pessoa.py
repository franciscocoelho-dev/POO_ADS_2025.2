class Pessoa:
    # Método de Inicialização
    def __init__(self, nome: str, idade: int):
        self.__nome = nome
        self.__idade = idade
    
    # Métodos Getter and Setters -->  get(pegar) e set(colocar)
    def get_nome(self):
        return self.__nome

    def set_nome(self, nome):
        self.__nome = nome

    def get_idade(self):
        return self.__idade
    
    def set_idade(self, idade):
        if idade > 0:
            self.__idade = idade


p1 = Pessoa('João', 30)
p1.set_nome('Maria')
p1.set_idade(28)

print(f'O {p1.get_nome()} tem {p1.get_idade()} anos')
