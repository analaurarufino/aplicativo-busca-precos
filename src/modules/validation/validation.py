class Validation:
    @staticmethod
    def validate_name(name):
        return bool(name)

    @staticmethod
    def validate_email(email):
        return "@" in email and "." in email

    @staticmethod
    def validate_password(password):
        return (
            8 <= len(password) <= 20
            and sum(c.isdigit() for c in password) >= 2
            and any(c.isalpha() for c in password)
        )