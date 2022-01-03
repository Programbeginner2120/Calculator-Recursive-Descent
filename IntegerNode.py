from Node import Node


class IntegerNode(Node):

    def __init__(self, num_value):
        self.num_value = int(num_value)
        self.exponent = None

    def get_integer_value(self):
        return self.num_value

    def __str__(self):
        string = f"{str(self.num_value)}"
        if self.exponent is not None:
            string += f"^{self.exponent}"
        return string

