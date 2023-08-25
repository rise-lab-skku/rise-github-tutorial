from .common import BinaryExpression


class AddExpression(BinaryExpression):
    def eval(self):
        return self.left.eval() + self.right.eval()


class MulExpression(BinaryExpression):
    def eval(self):
        return self.left.eval() * self.right.eval()
