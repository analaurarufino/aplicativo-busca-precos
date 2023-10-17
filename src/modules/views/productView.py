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

    def get_information_update(self, product):
        self.display_output("Digite as informações a serem atualizadas:")
        new_name = self.get_input(f"Nome ({product.name}): ") or product.name
        new_price = self.get_input(f"Preço ({product.price}): ") or product.price
        # new_category = self.get_input(f"Categoria ({product.subcategory}): ")

        data = Product(new_name, new_price, None)
        return data

    def print_products(self, products=[]):
        for i in products:
            self.display_output(products.get_data())
