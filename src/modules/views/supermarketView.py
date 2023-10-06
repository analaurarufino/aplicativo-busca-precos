from index import BaseView


class SupermarketView(BaseView):
    def get_information(self):
        self.display_output("Digite as informações do Supermercado: ")
        name = self.get_input("Nome: ")
        login = self.get_input("Login: ")
        password = self.get_input("Senha: ")
        cnpj = self.get_input("CNPJ: ")
        return {"name": name, "login": login, "password": password, "cnpj": cnpj}
