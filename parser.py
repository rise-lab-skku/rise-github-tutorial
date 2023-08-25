from tokenizer import (
    Tokenizer,
    ValueTokenType,
    PlusTokenType,
    MinusTokenType,
    MulTokenType,
    DivTokenType,
    LeftParenthesisTokenType,
    RightParenthesisTokenType,
    CosTokenType,
    SinTokenType,
    TanTokenType,
    ExpTokenType,
)

from expressions import (
    ValueExpression,
    AddExpression,
    MulExpression,
    PositiveExpression,
    NegativeExpression,
    InverseExpression,
    ParenthesisExpression,
    CosExpression,
    SinExpression,
    TanExpression,
    ExpExpression,
)


def create_parser():
    return Parser(
        Tokenizer(
            [
                ValueTokenType(),
                PlusTokenType(),
                MinusTokenType(),
                MulTokenType(),
                DivTokenType(),
                LeftParenthesisTokenType(),
                RightParenthesisTokenType(),
                CosTokenType(),
                SinTokenType(),
                TanTokenType(),
                ExpTokenType(),
            ]
        )
    )


class Parser:
    def __init__(self, tokenizer: Tokenizer):
        self.tokenizer = tokenizer

    def parse(self, text):
        self.tokenizer.set_text(text)
        return self.parse_expression()

    def parse_expression(self):
        term = self.parse_term()
        token = self.tokenizer.next()
        if token == None:
            return term
        elif token.type == "plus":
            self.tokenizer.advance()
            return AddExpression(term, self.parse_expression())
        elif token.type == "minus":
            self.tokenizer.advance()
            return AddExpression(term, self.parse_expression_neg())
        elif token.type == "right_parenthesis":
            self.tokenizer.advance()
            return term

    def parse_expression_neg(self):
        term = NegativeExpression(self.parse_term())
        token = self.tokenizer.next()
        if token == None:
            return term
        elif token.type == "plus":
            self.tokenizer.advance()
            return AddExpression(term, self.parse_expression())
        elif token.type == "minus":
            self.tokenizer.advance()
            return AddExpression(term, self.parse_expression_neg())
        elif token.type == "right_parenthesis":
            self.tokenizer.advance()
            return term

    def parse_term(self):
        factor = self.parse_factor()
        token = self.tokenizer.next()
        if token == None:
            return factor
        elif token.type == "mul":
            self.tokenizer.advance()
            return MulExpression(factor, self.parse_term())
        elif token.type == "div":
            self.tokenizer.advance()
            return MulExpression(factor, self.parse_term_inv())
        else:
            return factor

    def parse_term_inv(self):
        factor = InverseExpression(self.parse_factor())
        token = self.tokenizer.next()
        if token == None:
            return factor
        elif token.type == "mul":
            self.tokenizer.advance()
            return MulExpression(factor, self.parse_term())
        elif token.type == "div":
            self.tokenizer.advance()
            return MulExpression(factor, self.parse_term_inv())
        else:
            return factor

    def parse_factor(self):
        token = self.tokenizer.next()
        if token.type == "value":
            self.tokenizer.advance()
            return ValueExpression(token.value)
        elif token.type == "plus":
            self.tokenizer.advance()
            return PositiveExpression(self.parse_factor())
        elif token.type == "minus":
            self.tokenizer.advance()
            return NegativeExpression(self.parse_factor())
        elif token.type == "left_parenthesis":
            self.tokenizer.advance()
            return ParenthesisExpression(self.parse_expression())
        elif token.type == "cos":
            self.tokenizer.advance()
            return CosExpression(self.parse_factor())
        elif token.type == "sin":
            self.tokenizer.advance()
            return SinExpression(self.parse_factor())
        elif token.type == "tan":
            self.tokenizer.advance()
            return TanExpression(self.parse_factor())
        elif token.type == "exp":
            self.tokenizer.advance()
            return ExpExpression(self.parse_factor())
        else:
            raise Exception("parse error")
