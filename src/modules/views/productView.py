from modules.views.index import BaseView


class ProductView(BaseView):
    def get_information(self):
        self.display_output("Digite as informações do Produto: ")
        name = self.get_input("Nome: ")
        categoria = None  # Categoria ainda não é solicitada neste exemplo
        return {"name": name, "categoria": categoria}
