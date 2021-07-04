import Token as Tk
import IntegerNode as In
import FloatNode as Fn
import MathOperationNode as Mpn
import Calculate as Cal
import Lexer as Lx
import Parser as Pr

while 1:

    my_lexer = Lx.Lexer()

    expression = input("Enter math expression: ")
    try:
        my_lexer.lex(expression)
        for i in my_lexer.token_list:
            print(f"TOKEN: {i.token_enum}")
        my_parser = Pr.Parser(my_lexer.token_list)
        abstract_syntax_tree = my_parser.parse()
        print(abstract_syntax_tree)
        print(Cal.process_ast(abstract_syntax_tree))

    except Exception as e:
        print(e)

