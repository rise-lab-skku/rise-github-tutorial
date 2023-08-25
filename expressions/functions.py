from .common import UnaryExpression
import math


class CosExpression(UnaryExpression):
    def eval(self):
        return math.cos(self.context.eval())


class SinExpression(UnaryExpression):
    def eval(self):
        return math.sin(self.context.eval())


class TanExpression(UnaryExpression):
    def eval(self):
        return math.tan(self.context.eval())


class ExpExpression(UnaryExpression):
    def eval(self):
        return math.exp(self.context.eval())
