from funcionario import Funcionario
from departamento import Departamento

# Criação de Objetos Funcionario
func1 = Funcionario('Antonio', 'antonio@gmail.com')
func2 = Funcionario('Maria', 'maria@gmail.com')
func3 = Funcionario('João', 'joao@gmail.com')

# Criação do Objeto Departamento
depart1 = Departamento('Contabilidade')
depart1.adicionar_funcionario(func1)
depart1.adicionar_funcionario(func2)
depart1.adicionar_funcionario(func3)

print(depart1.exibir_funcionarios())


print('-' * 30)

