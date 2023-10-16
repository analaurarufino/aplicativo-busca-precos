from modules.views.index import BaseView
from modules.supermarket.supermarket import Supermarket

class SupermarketView(BaseView):
    def get_information(self):
        self.display_output("Digite as informações do Supermercado: ")
        name = self.get_input("Nome: ")
        email = self.get_input("Email: ")
        password = self.get_input("Senha: ")
        cnpj = self.get_input("CNPJ: ")
        data = Supermarket(name, email, password, cnpj)
        return data
    