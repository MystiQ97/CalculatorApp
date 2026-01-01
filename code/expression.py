from stack import Stack
from enum import Enum, IntEnum

def infix_to_postfix(infix: list):
    infix = infix
    postfix = []
    stack = Stack()

    for char in infix:
        if isinstance(char, Operand):
            postfix.append(char)

        elif isinstance(char, Operator):
            while (not stack.isEmpty()
                   and stack.peek().get_precedence() >= char.get_precedence()):
                postfix.append(stack.pop())
            stack.push(char)

    while not stack.isEmpty():
        postfix.append(stack.pop())

    return postfix


class OperatorPrecedence(IntEnum):

    LOWEST = 0
    ADD_OR_SUB = 1
    MULT_OR_DIV = 2
    POWER = 3
    BRACKETS = 4


class Operand:
    def __init__(self, data):
        self.data = data

    def __str__(self):
        return str(self.data)

    def get_data(self):
        return self.data


class Operator(Enum):

    START_BRACKET = '('
    END_BRACKET = ')'
    POWER = '^'
    MULTIPLY = '*'
    DIVIDE = '/'
    ADD = '+'
    SUBTRACT = '-'

    def __str__(self):
        return self.value

    def get_precedence(self):
        if self.value in ('+', '-'):
            return OperatorPrecedence.ADD_OR_SUB
        elif self.value in ('*', '/'):
            return OperatorPrecedence.MULT_OR_DIV
        elif self.value == '^':
            return OperatorPrecedence.POWER
        else:
            return OperatorPrecedence.BRACKETS

