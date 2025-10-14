from pessoa import Pessoa

class Medico(Pessoa):
    def __init__(self, nome, email, crm):
        super().__init__(nome, email)
        self.crm = crm

