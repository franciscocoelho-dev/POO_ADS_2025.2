class Fila: 

    fila_geral = []

    def __init__(self):
        self.pessoas = []
    
    def entrar_fila(self, nome):
        self.pessoas.append(nome)

    def sair_fila(self):
        self.pessoas.pop(0)

    def visualizar_fila(self):
        return self.pessoas
    
    @classmethod
    def entrar_fila_geral(cls, nome): 
        cls.fila_geral.append(nome)



# Criando um objeto do tipo Fila chamado supermercado
# supermercado = Fila()
# loteria = Fila()

# supermercado.entrar_fila('Ana')
# loteria.entrar_fila('Antonio')
# loteria.entrar_fila('Júlia')

# print(f'Fila do Supermercado: {supermercado.visualizar_fila()}')
# print(f'Fila da Loteria: {loteria.visualizar_fila()}')


Fila.entrar_fila_geral('Raimundo')


