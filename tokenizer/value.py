from .tokenizer import TokenType, Token


class ValueTokenType(TokenType):
    typename = "value"

    def check(self, tokenizer):
        if tokenizer.pos >= len(tokenizer.text):
            return None
        value = ""
        cur_pos = tokenizer.pos
        while tokenizer.text[cur_pos] in "0123456789.":
            value += tokenizer.text[cur_pos]
            cur_pos += 1
            if cur_pos >= len(tokenizer.text):
                break
        if value:
            tokenizer.pos = cur_pos
            return Token(ValueTokenType.typename, float(value))
