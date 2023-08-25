class Expression:
    def __init__(self, context):
        self.context = context


class UnaryExpression(Expression):
    def __init__(self, context):
        super().__init__(context)


class BinaryExpression(Expression):
    def __init__(self, left, right):
        self.left = left
        self.right = right
