import Token as Tk
from Error import MathSyntaxError
import re

NUMBER = re.compile("[0-9]")
PLUS = '+'
MINUS = '-'
TIMES = '*'
DIVIDE = '/'
EXPONENT = '^'
DECIMAL = '.'
LPAREN = '('
RPAREN = ')'

token_dict = {
    NUMBER: Tk.Token.TokenEnum.NUMBER,
    PLUS: Tk.Token.TokenEnum.PLUS,
    MINUS: Tk.Token.TokenEnum.MINUS,
    TIMES: Tk.Token.TokenEnum.TIMES,
    DIVIDE: Tk.Token.TokenEnum.DIVIDE,
    EXPONENT: Tk.Token.TokenEnum.EXPONENT,
    LPAREN: Tk.Token.TokenEnum.LPAREN,
    RPAREN: Tk.Token.TokenEnum.RPAREN
}


def match_token_type(ch):
    char_type = None
    if NUMBER.match(ch) or ch == DECIMAL:
        char_type = token_dict[NUMBER]
    else:
        char_type = token_dict.get(ch)
    return char_type


def determine_generation(calc_input, idx, curr_type=None):
    if idx == len(calc_input) - 1:
        return True
    if calc_input[idx] == ' ':
        return False
    next_char = calc_input[idx + 1]
    next_char_type = match_token_type(next_char)
    if next_char_type != curr_type or curr_type == next_char_type == Tk.Token.TokenEnum.MINUS:
        return True
    if next_char_type == curr_type:
        if curr_type == Tk.Token.TokenEnum.PLUS or curr_type == Tk.Token.TokenEnum.TIMES or curr_type == \
                Tk.Token.TokenEnum.DIVIDE or curr_type == Tk.Token.TokenEnum.EXPONENT:
            raise MathSyntaxError
    return False


class Lexer:

    def __init__(self):
        self.token_list = []

    def generate_token(self, token_type, value_str):
        value_str = value_str if value_str != "" else None
        self.token_list.append(Tk.Token(token_type, value_str))

    def handle_negatives(self):
        for idx, lexeme in enumerate(self.token_list):
            if lexeme.token_enum == Tk.Token.TokenEnum.MINUS:
                if idx < len(self.token_list):
                    if self.token_list[idx + 1].token_enum == Tk.Token.TokenEnum.NUMBER:
                        if idx == 0 or (self.token_list[idx - 1].token_enum == Tk.Token.TokenEnum.PLUS or
                                        self.token_list[idx - 1].token_enum == Tk.Token.TokenEnum.MINUS or
                                        self.token_list[idx - 1].token_enum == Tk.Token.TokenEnum.TIMES or
                                        self.token_list[idx - 1].token_enum == Tk.Token.TokenEnum.DIVIDE or
                                        self.token_list[idx - 1].token_enum == Tk.Token.TokenEnum.EXPONENT):
                            self.token_list[idx + 1].value_string = '-' + self.token_list[idx + 1].value_string
                            self.token_list.remove(lexeme)

    def lex(self, calc_input):
        token_type = False
        value_str = ""
        should_generate = None
        for i, ch in enumerate(calc_input):
            if ch == ' ':
                pass
            elif NUMBER.match(ch):
                token_type = token_dict[NUMBER]
            elif ch == DECIMAL:
                if '.' in value_str:
                    raise MathSyntaxError
                token_type = token_dict[NUMBER]
            elif ch == PLUS:
                token_type = token_dict[PLUS]
            elif ch == MINUS:
                token_type = token_dict[MINUS]
            elif ch == TIMES:
                token_type = token_dict[TIMES]
            elif ch == DIVIDE:
                token_type = token_dict[DIVIDE]
            elif ch == EXPONENT:
                token_type = token_dict[EXPONENT]
            elif ch == LPAREN:
                token_type = token_dict[LPAREN]
            elif ch == RPAREN:
                token_type = token_dict[RPAREN]
            else:
                raise MathSyntaxError
            if ch != ' ':
                value_str += ch
            if token_type is not None:
                should_generate = determine_generation(calc_input, i, token_type)
            else:
                should_generate = determine_generation(calc_input, i)
            if should_generate:
                self.generate_token(token_type, value_str)
                token_type = None
                value_str = ""
                should_generate = False
        self.handle_negatives()
