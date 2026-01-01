from expression import *

#TODO merge TreeNode with regular Node in stack.py
class TreeNode:
    def __init__(self, data = None, left_node = None, right_node = None):
        self.data = data
        self.left = left_node
        self.right = right_node


class BinaryExpressionTree:
    def __init__(self, expression = None):
        self.root = None
        self.stack = Stack()
        self.expression = expression
        if expression is not None:
            self.build_tree(expression)

    def build_tree(self, expression):
        for i in expression:
            if isinstance(i, Operand):
                self.stack.push(TreeNode(i))
            else:
                right_node = self.stack.pop()
                left_node = self.stack.pop()

                self.stack.push(TreeNode(i, left_node, right_node))

        self.root = self.stack.pop()

    def evaluate(self, root):
        if root is None:
            return 0

        if root.left is None and root.right is None:
            return root.data.get_data()

        left_sum = self.evaluate(root.left)
        right_sum = self.evaluate(root.right)

        match root.data:
            case Operator.ADD:
                return left_sum + right_sum
            case Operator.SUBTRACT:
                return left_sum - right_sum
            case Operator.MULTIPLY:
                return left_sum * right_sum
            case Operator.DIVIDE:
                return left_sum / right_sum



