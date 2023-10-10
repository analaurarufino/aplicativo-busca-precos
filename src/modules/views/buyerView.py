from modules.views.index import BaseView
from modules.buyer.buyer import Buyer


class BuyerView(BaseView):
    def get_information(self):
        self.display_output("Digite as informações do Comprador: ")
        name = self.get_input("Nome: ")
        email = self.get_input("Email: ")
        password = self.get_input("Senha: ")
        data = Buyer(name, email, password)
        return data
        #return {"name": name, "email": email, "password": password}
