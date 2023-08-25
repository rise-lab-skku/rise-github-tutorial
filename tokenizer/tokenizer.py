#! /usr/bin/env python3


class Token:
    def __init__(self, type: str, value: str):
        self.type = type
        self.value = value

    def __repr__(self):
        return f"token({self.type}, {self.value})"

    def __str__(self):
        return f"token({self.type}, {self.value})"


class TokenType:
    typename = "token_type"

    def __eq__(self, other) -> bool:
        return self.typename == other.typename

    def check(self, tokenizer):
        pass


class Tokenizer:
    def __init__(self, token_types: list):
        self.token_types = token_types
        self.text = ""
        self.pos = 0

    def set_text(self, text):
        self.text = text
        self.text = self.text.replace(" ", "")
        self.pos = 0
        self.prev_pos = 0

    def next(self) -> Token:
        if self.pos >= len(self.text):
            return None
        for token_type in self.token_types:
            self.pos = self.prev_pos
            token = token_type.check(self)
            if token:
                return token
        raise Exception("parse error")

    def advance(self):
        self.prev_pos = self.pos
