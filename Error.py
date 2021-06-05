class Error(Exception):
    """Base class for all other exceptions"""


class MathSyntaxError(Error):
    """Raised when input is of incorrect format"""

    def __init__(self, message="ERROR IN MATH SYNTAX"):
        self.message = message
        super().__init__(self.message)