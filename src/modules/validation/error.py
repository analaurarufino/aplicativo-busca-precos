class CustomError(Exception):
    def __init__(self, message="Um erro ocorreu."):
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        return f"Error: {self.message}"