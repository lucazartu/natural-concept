from .cadastroProduto import CadastroProduto

class ControladorProduto:
    def __init__(self):
        self.cadastroProduto = CadastroProduto()

    def listar(self, **kwargs):
        return self.cadastroProduto.listar(**kwargs)

    def adicionar_produto(self, **kwargs):
        try:
            self.cadastroProduto.adicionar_produto(**kwargs)
        except Exception as e:
            raise e

    def atualizar_produto(self, idProduto, **kwargs):
        try:
            self.cadastroProduto.atualizar_produto(idProduto, **kwargs)
        except Exception as e:
            raise e

    def remover_produto(self, **kwargs):
        try:
            self.cadastroProduto.remover_produto(**kwargs)
        except Exception as e:
            raise e