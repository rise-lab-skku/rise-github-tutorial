from .common import UnaryExpression


class ValueExpression(UnaryExpression):
    def eval(self):
        return float(self.context)


class PositiveExpression(UnaryExpression):
    def eval(self):
        return self.context.eval()


class NegativeExpression(UnaryExpression):
    def eval(self):
        return -self.context.eval()


class InverseExpression(UnaryExpression):
    def eval(self):
        return 1 / self.context.eval()
