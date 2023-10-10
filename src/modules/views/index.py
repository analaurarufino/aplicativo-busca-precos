from abc import ABC, abstractmethod


class BaseView(ABC):
    def __init__(self, input_function, print_function):
        self.input_function = input_function
        self.print_function = print_function

    @abstractmethod
    def get_information(self):
        pass

    def get_input(self, message):
        return self.input_function(message)

    def display_output(self, output):
        self.print_function(output)
