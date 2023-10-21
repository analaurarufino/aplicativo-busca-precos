class Validation:
    @staticmethod
    def validate_name(name):
        if not (5 <= len(name) <= 50):
            raise ValueError("Comprimento de nome inválido. O nome deve ter entre 5 e 50 caracteres.")

    @staticmethod
    def validate_price(price):
        if not (isinstance(price, (int, float)) and price >= 0):
            raise ValueError("Valor de preço inválido. O preço deve ser um número não negativo.")

    @staticmethod
    def validate_subcategory(subcategory):
        # Você pode adicionar sua própria lógica de validação para a subcategoria aqui.
        if not (isinstance(subcategory, str) and len(subcategory) <= 50):
            raise ValueError("Valor de subcategoria inválido.")
        
    @staticmethod
    def validate_email(email):
        if not ("@" in email and "." in email):
            raise ValueError("Formato de email inválido.")

    @staticmethod
    def validate_password(password):
        if not (
            8 <= len(password) <= 20
            and sum(c.isdigit() for c in password) >= 2
            and any(c.isalpha() for c in password)
        ):
            raise ValueError("Formato de senha inválido. A senha deve ter de 8 a 20 caracteres, com pelo menos 2 dígitos e pelo menos 1 letra.")

    @staticmethod
    def validate_cnpj(cnpj):
        cnpj = ''.join(filter(str.isdigit, cnpj))

        if not (len(cnpj) == 14 and cnpj.isnumeric()):
            raise ValueError("Formato de CNPJ inválido. O CNPJ deve ter exatamente 14 dígitos.")

        cnpj = [int(digit) for digit in cnpj]
        calc1 = (
            cnpj[0] * 5 + cnpj[1] * 4 + cnpj[2] * 3 +
            cnpj[3] * 2 + cnpj[4] * 9 + cnpj[5] * 8 +
            cnpj[6] * 7 + cnpj[7] * 6 + cnpj[8] * 5 +
            cnpj[9] * 4 + cnpj[10] * 3 + cnpj[11] * 2
        )
        remainder1 = calc1 % 11

        if remainder1 < 2:
            if cnpj[12] != 0:
                raise ValueError("CNPJ inválido. Verifique o número do CNPJ.")
        else:
            if cnpj[12] != 11 - remainder1:
                raise ValueError("CNPJ inválido. Verifique o número do CNPJ.")

        calc2 = (
            cnpj[0] * 6 + cnpj[1] * 5 + cnpj[2] * 4 +
            cnpj[3] * 3 + cnpj[4] * 2 + cnpj[5] * 9 +
            cnpj[6] * 8 + cnpj[7] * 7 + cnpj[8] * 6 +
            cnpj[9] * 5 + cnpj[10] * 4 + cnpj[11] * 3 + cnpj[12] * 2
        )
        remainder2 = calc2 % 11

        if remainder2 < 2:
            if cnpj[13] != 0:
                raise ValueError("CNPJ inválido. Verifique o número do CNPJ.")
        else:
            if cnpj[13] != 11 - remainder2:
                raise ValueError("CNPJ inválido. Verifique o número do CNPJ.")
