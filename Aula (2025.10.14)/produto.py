from rastreavel import RastreavelMixin

class Produto:
    # Atributo de Classe
    gerador_codigo = 0

    # Método de Inicializacao
    def __init__(self, descricao: str, quant: int, valor: float) -> None:
        # Incrementar o gerador_codigo em +1, e atribuir o novo valor
        # ao atributo __codigo
        Produto.gerador_codigo += 1
        self.__codigo = Produto.gerador_codigo 
        self.__descricao = descricao
        self.__quant = quant
        self.__valor = valor
    
    # Métodos Getters
    @property
    def codigo(self) -> int:
        return self.__codigo
    
    @property
    def descricao(self) -> str:
        return self.__descricao
    
    @property
    def quant(self) -> int:
        return self.__quant

    @property
    def valor(self) -> float:
        return self.__valor

    # Método Setters
    @descricao.setter
    def descricao(self, nova_descricao: str) -> None:
        # strip() -> remove os espaços vazios antes e depois
        # len() -> conta os caracteres
        if len(nova_descricao.strip()) >= 5:
            self.__descricao = nova_descricao.strip()
    
    @quant.setter
    def quant(self, quant_adicional: int) -> None:
        # isinstance() vai verificar se a quant_adicional é do tipo int
        if quant_adicional > 0 and isinstance(quant_adicional, int):
            self.__quant += quant_adicional
    
    @valor.setter
    def valor(self, novo_valor: float) -> None:
        if novo_valor > 0:
            self.__valor = novo_valor

    





