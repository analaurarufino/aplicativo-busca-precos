from modules.views.index import BaseView


class BuyerView(BaseView):
    def get_information(self):
        self.display_output("Digite as informações do Comprador: ")
        name = self.get_input("Nome: ")
        email = self.get_input("Email: ")
        password = self.get_input("Senha: ")
        return {"name": name, "email": email, "password": password}
