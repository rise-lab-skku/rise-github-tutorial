from .tokenizer import TokenType, Token


class CosTokenType(TokenType):
    typename = "cos"

    def check(self, tokenizer):
        if (tokenizer.pos + 2) >= len(tokenizer.text):
            return None
        if tokenizer.text[tokenizer.pos : tokenizer.pos + 3] == "cos":
            tokenizer.pos += 3
            return Token(CosTokenType.typename, "cos")
        return None


class SinTokenType(TokenType):
    typename = "sin"

    def check(self, tokenizer):
        if (tokenizer.pos + 2) >= len(tokenizer.text):
            return None
        if tokenizer.text[tokenizer.pos : tokenizer.pos + 3] == "sin":
            tokenizer.pos += 3
            return Token(SinTokenType.typename, "sin")
        return None


class TanTokenType(TokenType):
    typename = "tan"

    def check(self, tokenizer):
        if (tokenizer.pos + 2) >= len(tokenizer.text):
            return None
        if tokenizer.text[tokenizer.pos : tokenizer.pos + 3] == "tan":
            tokenizer.pos += 3
            return Token(TanTokenType.typename, "tan")
        return None


class ExpTokenType(TokenType):
    typename = "exp"

    def check(self, tokenizer):
        if (tokenizer.pos + 2) >= len(tokenizer.text):
            return None
        if tokenizer.text[tokenizer.pos : tokenizer.pos + 3] == "exp":
            tokenizer.pos += 3
            return Token(ExpTokenType.typename, "exp")
        return None
