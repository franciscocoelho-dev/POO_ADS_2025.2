class Aluno:
    # Método de Inicialização
    def __init__(self, nome, email):
        self.nome = nome
        self.email = email

    # Getter
    @property
    def nome(self):
        return self._nome

    # Setter
    @nome.setter
    def nome(self, novo_nome):
        if len(novo_nome) >= 3:
            print('Estou passando dentro do setter')
            self._nome = novo_nome


aluno1 = Aluno('Antonio', 'antonio@gmail.com')
aluno1.nome = 'Antonio Silva'
print(aluno1.nome)

