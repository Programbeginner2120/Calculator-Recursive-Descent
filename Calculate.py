import Node
import FloatNode as Fl
import IntegerNode as In
import MathOperationNode as Mop
import Token as Tk
from Error import MathSyntaxError


def process_ast(ast: Node):
    return process_add_subtract(ast)


def process_add_subtract(current_node: Node):
    if current_node is None:
        return None
    if isinstance(current_node, Mop.MathOpNode):
        left_node = process_add_subtract(current_node.left_node)
        right_node = process_add_subtract(current_node.right_node)
        exp = process_add_subtract(current_node.exponent)
        if current_node.operation_type == Tk.Token.TokenEnum.PLUS:
            rv = (left_node + right_node) ** exp if exp is not None else left_node + right_node
            return rv
        elif current_node.operation_type == Tk.Token.TokenEnum.MINUS:
            rv = (left_node - right_node) ** exp if exp is not None else left_node - right_node
            return rv
    return process_multiply_divide(current_node)


def process_multiply_divide(current_node: Node):
    if current_node is None:
        return None
    if isinstance(current_node, Mop.MathOpNode):
        left_node = process_add_subtract(current_node.left_node)
        right_node = process_add_subtract(current_node.right_node)
        exp = process_add_subtract(current_node.exponent)
        if current_node.operation_type == Tk.Token.TokenEnum.TIMES:
            rv = (left_node * right_node) ** exp if exp is not None else left_node * right_node
            return rv
        elif current_node.operation_type == Tk.Token.TokenEnum.DIVIDE:
            rv = (left_node / right_node) ** exp if exp is not None else left_node / right_node
            return rv
    return process_int_float(current_node)


def process_int_float(current_node: Node):
    exp = process_add_subtract(current_node.exponent)
    rv = current_node.num_value ** exp if current_node.exponent is not None else current_node.num_value
    return rv