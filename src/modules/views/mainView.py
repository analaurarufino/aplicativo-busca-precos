import curses
from modules.views.index import BaseView

class MenuView(BaseView):
    def __init__(self, input_function, print_function):
        super().__init__(input_function, print_function)

    def get_information(self):
        selected_option = None
        options = ["Adicionar Comprador","Adicionar Supermercado","Adicionar Produtos", "Sair"]
        current_option = 0

        # Inicializa a tela curses
        stdscr = curses.initscr()
        curses.curs_set(0)  # Esconde o cursor

        # Configura a tela para aceitar input das setas
        stdscr.keypad(1)
        stdscr.clear()

        while selected_option is None:
            stdscr.clear()
            stdscr.addstr("Selecione uma opção:\n")

            # Exibe as opções com destaque na opção atual
            for i, option in enumerate(options):
                if i == current_option:
                    stdscr.addstr(f"> {i + 1} - {option}\n")
                else:
                    stdscr.addstr(f"  {i + 1} - {option}\n")

            # Aguarda a entrada do usuário
            key = stdscr.getch()

            if key == curses.KEY_UP and current_option > 0:
                current_option -= 1
            elif key == curses.KEY_DOWN and current_option < len(options) - 1:
                current_option += 1
            elif key == 10:  # Tecla Enter
                selected_option = current_option + 1

        # Restaura a configuração da tela
        curses.endwin()
        return selected_option