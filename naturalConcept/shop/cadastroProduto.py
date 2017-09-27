from .models import Product

class CadastroProduto:

    def listar(self, **kwargs):
        return Product.objects.filter(**kwargs)

    def adicionar_produto(self, **kwargs):
        try:
            Product.objects.create(**kwargs)
        except Exception as e:
            raise e

    def atualizar_produto(self, idProduto, **kwargs):
        try:
            Product.objects.filter(id=idProduto).update(**kwargs)
        except Exception as e:
            raise e

    def remover_produto(self, **kwargs):
        try:
            products = Product.objects.filter(**kwargs)
            products.delete()
        except Exception as e:
            raise e