from .common import UnaryExpression


class ParenthesisExpression(UnaryExpression):
    def eval(self):
        return self.context.eval()
