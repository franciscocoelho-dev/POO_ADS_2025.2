# OBS: Todas as linhas iniciadas com # são compreendidas pela Python como um comentário,
#      e não serão executadas como código.


class Fila: 

    # O atributo "quant_filas" está fora do método especial __init__(), logo esse atributo deixa de
    # ficar no escopo do objeto e passa a ficar no escopo da classe.
    quant_filas = 0

    def __init__(self):
        self.pessoas = []

    def entrar_fila(self, nome):
        self.pessoas.append(nome)

    def sair_fila(self):
        self.pessoas.pop(0)

    def visualizar_fila(self):
        return self.pessoas


    # O método adicionar_fila incrementa em uma unidade o atributo de classe quant_filas. 
    # A convenção do Python é usar cls para o primeiro parâmetro de métodos de classe, o
    # que representa a própria classe Fila, permitindo que o método acesse e modifique atributos
    # no escopo da classe.

    # O @classmethod é um decorador em Python que transforma um método comum em um método de classe.

    @classmethod
    def adicionar_fila(cls):
        cls.quant_filas += 1

    # A principal função de visualizar_filas é acessar e exibir o número total de filas que foram
    #  criadas. Ele não modifica o estado da classe, apenas retorna o valor de um atributo de classe.

    @classmethod
    def visualizar_filas(cls):
        return cls.quant_filas




# Adicionando uma unidade ao atributo de classe "quant_filas"
Fila.adicionar_fila()

# Visualizando o valor do atributo de classe "quant_filas"
print(Fila.visualizar_filas())