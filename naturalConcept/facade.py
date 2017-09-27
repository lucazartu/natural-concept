from shop.controladorProduto import ControladorProduto

class Fachada:

    def __init__(self):
        self.controladorProduto = ControladorProduto()

    def listar(self, **kwargs):
        return self.controladorProduto.listar(**kwargs)

    def adicionar_produto(self, **kwargs):
        try:
            self.controladorProduto.adicionar_produto(**kwargs)
        except Exception as e:
            raise e

    def atualizar_produto(self, idProduto, **kwargs):
        try:
            self.controladorProduto.atualizar_produto(idProduto=idProduto, **kwargs)
        except Exception as e:
            raise e
    def remover_produto(self, **kwargs):
        try:
            self.controladorProduto.remover_produto(**kwargs)
        except Exception as e:
            raise e
