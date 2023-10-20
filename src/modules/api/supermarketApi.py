from modules.api.adapter import SupermarketAPIAdapter
import requests
from modules.product.product import Product

# Exemplo de uso APIs de supermercados extenos:
class SupermarketAPIConnect(SupermarketAPIAdapter):
    def __init__(self, api_base_url):
        self.api_base_url = api_base_url

    def get_product_info(self, product_id):
        # Exemplo de chamada para pegar as informações dos produtos
        products = []
        response = requests.get(f"{self.api_base_url}/products/{product_id}")
        if response.status_code == 200:
            data = response.json()
            product_name = data.get('product_name', '')
            product_price = data.get('product_price', 0)

        # Crie uma instância da classe Product com os dados da API
            product = Product(name=product_name, price=product_price, subcategory=None)
            products.append(product)

            return products
  
        else:
            return None
