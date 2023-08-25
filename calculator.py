#!/usr/bin/env python3
from parser import create_parser


class CalculatorCLI:
    def __init__(self, parser):
        self.parser = parser

    def run(self):
        while True:
            try:
                text = input("calc> ")
            except EOFError:
                return 0
            except KeyboardInterrupt:
                return 0
            except:
                return 1
            if not text:
                continue
            expr = self.parser.parse(text)
            print(expr.eval())
        return 0


if __name__ == "__main__":
    app = CalculatorCLI(create_parser())
    exit(app.run())
