from modules.views.index import BaseView
from modules.product.product import Product


class ProductView(BaseView):
    def get_information(self):
        self.display_output("Digite as informações do Produto: ")
        name = self.get_input("Nome: ")
        price = self.get_input("Preço: ")
        categoria = None  # Categoria ainda não é solicitada neste exemplo
        data = Product(name, price, categoria)
        return data
