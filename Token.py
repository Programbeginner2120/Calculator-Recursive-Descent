import enum as e


class Token:

    class TokenEnum(e.Enum):
        NUMBER = "NUMBER"
        PLUS = "PLUS"
        MINUS = "MINUS"
        TIMES = "TIMES"
        DIVIDE = "DIVIDE"
        EXPONENT = "EXPONENT"
        LPAREN = "LPAREN"
        RPAREN = "RPAREN"

    def __init__(self, token_enum, value_string=None):
        self.token_enum = token_enum
        self.value_string = value_string

    def get_token_enum(self):
        return self.token_enum

    def get_value_string(self):
        return self.value_string

    def __str__(self):
        return f"Token: {self.token_enum}\nValue String: {self.value_string}"

