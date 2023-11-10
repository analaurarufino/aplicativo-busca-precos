#Padrão builder

class CustomError(Exception):
    def __init__(self, message="Um erro ocorreu."):
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        return f"Error: {self.message}"

class ErrorBuilder:
    def __init__(self, base_message="Um erro ocorreu."):
        self.custom_error = CustomError(base_message)

    def add_details(self, details):
        self.custom_error.message += f" Detalhes: {details}"
        return self

    def add_code(self, error_code):
        self.custom_error.message += f" Código do erro: {error_code}"
        return self

    def build(self):
        return self.custom_error

