class Validation:
    @staticmethod
    def validate_name(name):
        if not (5 <= len(name) <= 50):
            raise ValueError("Invalid name length. Name must be between 5 and 50 characters.")

    @staticmethod
    def validate_price(price):
        if not (isinstance(price, (int, float)) and price >= 0):
            raise ValueError("Invalid price value. Price must be a non-negative number.")

    @staticmethod
    def validate_subcategory(subcategory):
        # You can add your own validation logic for the subcategory here.
        if not (isinstance(subcategory, str) and len(subcategory) <= 50):
            raise ValueError("Invalid subcategory value.")
        
    @staticmethod
    def validate_email(email):
        if not ("@" in email and "." in email):
            raise ValueError("Invalid email format.")

    @staticmethod
    def validate_password(password):
        if not (
            8 <= len(password) <= 20
            and sum(c.isdigit() for c in password) >= 2
            and any(c.isalpha() for c in password)
        ):
            raise ValueError("Invalid password format. Password must be 8-20 characters with at least 2 digits and at least 1 letter.")


