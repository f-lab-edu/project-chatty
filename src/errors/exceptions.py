class InvalidStateException(Exception):
    def __init__(self, expression: str):
        self.expression = expression
