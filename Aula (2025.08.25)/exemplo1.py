# OBS: Todas as linhas iniciadas com # são compreendidas pela Python como um comentário,
#      e não serão executadas como código.


class Fila: 

    # Método __init__() é o local onde definimos as "configurações" iniciais de um objeto.
    # Nesse método é possível definir os atributos e seus valores iniciais.
    # No exemplo do __init__() abaixo, todo objeto criado a partir da classe Fila terá uma lista
    # chamada de pessoas.

    def __init__(self):
        self.pessoas = []
    
    # O valor self dentro do parâmetro () do método representa "my self -> (eu mesmo)", definindo
    # que o método é acessado por objetos, e não por referências à classe.
    # No método abaixo, quem chamar deve informar um nome, que será adicionado a lista de pessoas
    # do objeto criado a partir da classe Fila.

    def entrar_fila(self, nome):
        self.pessoas.append(nome)

    # O método sair_fila não precisa de informação obrigatória para ser executado, logo temos apenas
    # o self no (), definindo o seu uso por meio de objetos Fila. O método pop() remove um elemento da
    # lista. Ao colocar o ZERO como valor do parâmetro (), significa que estamos removendo o 1º elemento
    # da lista de pessoas.

    def sair_fila(self):
        self.pessoas.pop(0)

    # O método visualizar_fila retorna (return) a lista de pessoas do objeto que chamar o método. Ele
    # apenas retorna, não exibe. Quem o chamou que deve imprimir (print) os valores.

    def visualizar_fila(self):
        return self.pessoas




# Criando um objeto supermercado do tipo Fila, que tem tudo que configuramos acima na classe.
supermercado = Fila()

# Inserindo pessoas na fila do supermercado
supermercado.entrar_fila('Ana')
supermercado.entrar_fila('João')
supermercado.entrar_fila('Maria')

# Removendo uma pessoa da Fila do supermercado
supermercado.sair_fila()

# Mostrando a Fila de pessoas
print(supermercado.visualizar_fila())

