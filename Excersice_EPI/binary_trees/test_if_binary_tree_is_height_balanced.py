import collections

from binary_tree import BinaryTreeNode

A = BinaryTreeNode("A")
B = BinaryTreeNode("B")
C = BinaryTreeNode("C")
D = BinaryTreeNode("D")
E = BinaryTreeNode("E")
F = BinaryTreeNode("F")
G = BinaryTreeNode("G")
H = BinaryTreeNode("H")
I = BinaryTreeNode("I")
J = BinaryTreeNode("J")
K = BinaryTreeNode("K")
L = BinaryTreeNode("L")
M = BinaryTreeNode("M")
N = BinaryTreeNode("N")
O = BinaryTreeNode("O")
#X = BinaryTreeNode("X")

A.left = B
A.right = K
B.left = C
B.right = H
C.left = D
C.right = G
D.left = E
D.right = F
H.left = I
H.right = J
K.left = L
K.right = O
L.left = M
L.right = N
#M.left = X

A.print_tree()


def is_balanced_binary_tree(tree: BinaryTreeNode) -> bool:
    BalancedStatusWithHeight = collections.namedtuple('BalancedStatusWithHeight', ('balanced', 'height'))
    def check_balanced(tree):
        if not tree:
            return BalancedStatusWithHeight(balanced=True, height=-1)

        left_result = check_balanced(tree.left)
        if not left_result.balanced:
            return left_result

        right_result = check_balanced(tree.right)
        if not right_result.balanced:
            return right_result

        is_balanced = abs(left_result.height - right_result.height) <= 1
        height = max(left_result.height, right_result.height) + 1
        return BalancedStatusWithHeight(is_balanced, height)

    return check_balanced(tree).balanced

print("Binary Tree is height-balanced: " + str(is_balanced_binary_tree(A)))
