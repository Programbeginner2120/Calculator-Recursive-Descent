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
        if current_node.operation_type == Tk.Token.TokenEnum.PLUS:
            return left_node + right_node
        elif current_node.operation_type == Tk.Token.TokenEnum.MINUS:
            return left_node - right_node
    return process_multiply_divide(current_node)


def process_multiply_divide(current_node: Node):
    if current_node is None:
        return None
    if isinstance(current_node, Mop.MathOpNode):
        left_node = process_add_subtract(current_node.left_node)
        right_node = process_add_subtract(current_node.right_node)
        if current_node.operation_type == Tk.Token.TokenEnum.TIMES:
            return left_node * right_node
        elif current_node.operation_type == Tk.Token.TokenEnum.DIVIDE:
            return left_node / right_node
    return process_int_float(current_node)


def process_int_float(current_node: Node):
    return current_node.num_value