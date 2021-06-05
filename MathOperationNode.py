from Node import Node
import Token as Tk


class MathOpNode(Node):

    def __init__(self, operation_type: Tk.Token.TokenEnum, left_node, right_node):
        self.operation_type = operation_type
        self.left_node = left_node
        self.right_node = right_node
        self.exponent = None

    def __str__(self):
        string = f"MathOpNode({self.operation_type}, {self.left_node}, {self.right_node})"
        if self.exponent is not None:
            string += f"^{self.exponent}"
        return string