class Departamento:
    # Método de Inicialização
    def __init__(self, nome):
        self.nome = nome
        self.lista_funcionario = []
    
    def adicionar_funcionario(self, funcionario):
        self.lista_funcionario.append(funcionario)
    
    # Sugestão: Método de remoção

    def exibir_funcionarios(self):
        funcionarios = ''
        for funcionario in self.lista_funcionario:
            funcionarios += f'{funcionario.nome}({funcionario.email})\n'
        return funcionarios

    def __del__(self):
        print(f'Foi removido da memória o departamento {self.nome}')


