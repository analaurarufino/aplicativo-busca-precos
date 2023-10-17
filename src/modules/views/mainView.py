from modules.views.index import BaseView


class MenuView(BaseView):
    def __init__(self, input_function, print_function):
        super().__init__(input_function, print_function)

    def get_information(self):
        selected_option = None
        options = [
            "Adicionar Comprador",
            "Adicionar Supermercado",
            "Adicionar Produtos",
            "Atualizar Produto",
            "Listar todos os produtos",
            "Excluir Produto",
            "Sair",
        ]

        while selected_option is None:
            print("Selecione uma opção:")

            # Exibe as opções com números
            for i, option in enumerate(options):
                print(f"{i + 1}. {option}")

            try:
                # Aguarda a entrada do usuário
                user_input = int(input("Digite o número da opção desejada: "))

                if 1 <= user_input <= len(options):
                    selected_option = user_input
                else:
                    print("Opção inválida. Tente novamente.")
            except ValueError:
                print("Entrada inválida. Digite um número.")

        return selected_option

    def get_id(self):
        idTable = self.input_function("Digite o ID: ")
        return idTable

    def display_info(self, men):
        self.print_function(men)
