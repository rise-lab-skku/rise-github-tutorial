from .tokenizer import TokenType, Token


class LeftParenthesisTokenType(TokenType):
    typename = "left_parenthesis"

    def check(self, tokenizer):
        if tokenizer.pos >= len(tokenizer.text):
            return None
        if tokenizer.text[tokenizer.pos] == "(":
            tokenizer.pos += 1
            return Token(LeftParenthesisTokenType.typename, "(")
        return None


class RightParenthesisTokenType(TokenType):
    typename = "right_parenthesis"

    def check(self, tokenizer):
        if tokenizer.pos >= len(tokenizer.text):
            return None
        if tokenizer.text[tokenizer.pos] == ")":
            tokenizer.pos += 1
            return Token(RightParenthesisTokenType.typename, ")")
        return None
