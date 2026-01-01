from tree import BinaryExpressionTree
from expression import *

def main():
    infix = [
        Operand(10),
        Operator.ADD,
        Operand(2),
        Operator.MULTIPLY,
        Operand(5),
        Operator.DIVIDE,
        Operand(2)
    ]

    postfix = infix_to_postfix(infix)
    for char in postfix:
        print(char)

    tree = BinaryExpressionTree(postfix)
    print("")
    print(tree.evaluate(tree.root))


if __name__ == '__main__':
    main()




