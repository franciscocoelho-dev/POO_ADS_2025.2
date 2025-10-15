from produto import Produto

class RastreavelMixin:

    registros_movimentacao = []

    def mover_produto(self, produto: Produto, quant: int, origem: str, destino: str) -> None:
        self.movimentacao = {
            'produto': produto,
            'quant': quant,
            'origem': origem,
            'destino': destino
        }
        RastreavelMixin.registros_movimentacao.append(self.movimentacao)



