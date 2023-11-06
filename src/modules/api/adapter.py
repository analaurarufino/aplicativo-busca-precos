#Classe para adaptar APIs de supermercados 
#para atualizar os valores dos produtos diretamente
from modules.product.product import Product
def fetch():
    pass

class SupermarketAPIAdapter:
    def __init__(self, url) -> None:
        self.url = url

    def get_product_info(self):
        response = fetch(self.url)
        products = []

        for item in response:
            product = Product(item['product_name'], item['product_price'], item['product_subcategory'])
            products.append(product.get_data())


