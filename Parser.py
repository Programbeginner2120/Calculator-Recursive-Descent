import Node
import FloatNode as Fl
import IntegerNode as In
import MathOperationNode as Mop
import Token as Tk
from Error import MathSyntaxError


class Parser:

    def __init__(self, token_list):
        self.token_list = token_list


    def parse(self) -> Node:
        return self.expression()


    def match_and_remove(self, desired_token_type: Tk.Token.TokenEnum) -> Tk.Token:
        if not self.token_list:
            return None
        if self.token_list[0].token_enum == desired_token_type:
            token = self.token_list[0]
            self.token_list.remove(token)
            return token
        return None


    def expression(self) -> Node:
        current_node = self.term()
        if current_node is not None:
            return self.get_right_of_expression(current_node)
        return None


    def get_right_of_expression(self, left_node: Node) -> Node:
        operator_token = self.match_and_remove(Tk.Token.TokenEnum.PLUS)
        operator_token = self.match_and_remove(Tk.Token.TokenEnum.MINUS) if operator_token is None else operator_token

        if operator_token is None:
            return left_node

        right_node = self.term()

        if right_node is None:
            print("Found + or - without right hand element")
            raise Exception

        operation_node = Mop.MathOpNode(operator_token.token_enum, left_node, right_node)

        return self.get_right_of_expression(operation_node)


    def term(self) -> Node:
        current_node = self.factor()
        if current_node is not None:
            return self.get_right_of_term(current_node)
        return None


    def get_right_of_term(self, left_node: Tk.Token) -> Node:
        operator_token = self.match_and_remove(Tk.Token.TokenEnum.TIMES)
        operator_token = self.match_and_remove(Tk.Token.TokenEnum.DIVIDE) if operator_token is None else operator_token

        if operator_token is None:
            return left_node

        right_node = self.factor()

        if right_node is None:
            print("Found * or / without right hand element")
            raise Exception

        operation_node = Mop.MathOpNode(operator_token.token_enum, left_node, right_node)

        return self.get_right_of_term(operation_node)


    def factor(self) -> Node:
        generated_node = None
        exponent_of_node = None

        removed_token = self.match_and_remove(Tk.Token.TokenEnum.NUMBER)

        if removed_token is not None:
            if self.match_and_remove(Tk.Token.TokenEnum.EXPONENT) is not None:
                exponent_of_node = self.factor()
                if exponent_of_node is None:
                    print("Found exponent without any expression following")
                    raise Exception
            if '.' in removed_token.value_string:
                generated_node = Fl.FloatNode(removed_token.value_string)
            else:
                generated_node = In.IntegerNode(removed_token.value_string)
            generated_node.exponent = exponent_of_node
            return generated_node


        if self.match_and_remove(Tk.Token.TokenEnum.LPAREN) is not None:
            processed_expression = self.expression()
            if processed_expression is not None:
                if self.match_and_remove(Tk.Token.TokenEnum.RPAREN) is not None:
                    if self.match_and_remove(Tk.Token.TokenEnum.EXPONENT) is not None:
                        exponent_of_node = self.factor()
                        if exponent_of_node is None:
                            print("Found exponent without any expression following")
                            raise Exception
                    generated_node = processed_expression
                    generated_node.exponent = exponent_of_node
                    return generated_node
                print("Found left parenthesis and expression without right parenthesis")
                raise Exception
            print("Found right parenthesis without required expression")
            raise Exception