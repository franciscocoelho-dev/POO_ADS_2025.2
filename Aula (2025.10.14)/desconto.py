class DescontoMixin:

    desconto_padrao = 0.10

    def gerar_desconto(self, valor):
        return valor - (valor * DescontoMixin.desconto_padrao)
    
