from .tokenizer import TokenType, Token


class PlusTokenType(TokenType):
    typename = "plus"

    def __init__(self):
        self.id = "plus"

    def check(self, tokenizer):
        if tokenizer.pos >= len(tokenizer.text):
            return None
        if tokenizer.text[tokenizer.pos] == "+":
            tokenizer.pos += 1
            return Token(PlusTokenType.typename, "+")
        return None


class MinusTokenType(TokenType):
    typename = "minus"

    def check(self, tokenizer):
        if tokenizer.pos >= len(tokenizer.text):
            return None
        if tokenizer.text[tokenizer.pos] == "-":
            tokenizer.pos += 1
            return Token(MinusTokenType.typename, "-")
        return None


class MulTokenType(TokenType):
    typename = "mul"

    def check(self, tokenizer):
        if tokenizer.pos >= len(tokenizer.text):
            return None
        if tokenizer.text[tokenizer.pos] == "*":
            tokenizer.pos += 1
            return Token(MulTokenType.typename, "*")
        return None


class DivTokenType(TokenType):
    typename = "div"

    def check(self, tokenizer):
        if tokenizer.pos >= len(tokenizer.text):
            return None
        if tokenizer.text[tokenizer.pos] == "/":
            tokenizer.pos += 1
            return Token(DivTokenType.typename, "/")
        return None
