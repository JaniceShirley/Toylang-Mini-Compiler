# AST Nodes
class LetNode:
    def __init__(self, name, value):
        self.name = name
        self.value = value

class PrintNode:
    def __init__(self, expression):
        self.expression = expression

class AddNode:
    def __init__(self, left, right):
        self.left = left
        self.right = right

class SubNode:
    def __init__(self, left, right):
        self.left = left
        self.right = right

class MulNode:
    def __init__(self, left, right):
        self.left = left
        self.right = right

class DivNode:
    def __init__(self, left, right):
        self.left = left
        self.right = right


class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.pos = 0

    def current(self):
        return self.tokens[self.pos]

    def eat(self, token_type):
        token = self.current()
        if token[0] == token_type:
            self.pos += 1
            return token[1]
        raise SyntaxError(f"Expected {token_type}, got {token[0]}")

    def parse_expression(self):
        # first value (number or variable)
        if self.current()[0] == "NUMBER":
            left = self.eat("NUMBER")
        else:
            left = self.eat("IDENTIFIER")

        # check if math operator exists
        if self.pos < len(self.tokens):
            token_type = self.current()[0]

            if token_type == "PLUS":
                self.eat("PLUS")
                right = self.eat("IDENTIFIER")
                return AddNode(left, right)

            elif token_type == "MINUS":
                self.eat("MINUS")
                right = self.eat("IDENTIFIER")
                return SubNode(left, right)

            elif token_type == "MULTIPLY":
                self.eat("MULTIPLY")
                right = self.eat("IDENTIFIER")
                return MulNode(left, right)

            elif token_type == "DIVIDE":
                self.eat("DIVIDE")
                right = self.eat("IDENTIFIER")
                return DivNode(left, right)

        return left

    def parse(self):
        statements = []

        while self.pos < len(self.tokens):
            if self.current()[0] == "LET":
                statements.append(self.parse_let())
            elif self.current()[0] == "PRINT":
                statements.append(self.parse_print())

        return statements

    def parse_let(self):
        self.eat("LET")
        name = self.eat("IDENTIFIER")
        self.eat("EQUAL")
        value = self.parse_expression()
        return LetNode(name, value)

    def parse_print(self):
        self.eat("PRINT")
        expr = self.parse_expression()
        return PrintNode(expr)