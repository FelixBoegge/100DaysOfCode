from binary_tree import BinaryTreeNode


A = BinaryTreeNode(314)
B = BinaryTreeNode(6)
C = BinaryTreeNode(2)
D = BinaryTreeNode(3)
E = BinaryTreeNode(6)
F = BinaryTreeNode(2)
G = BinaryTreeNode(3)

A.left = B
A.right = E
B.right = C
C.right = D
E.left = F
F.left = G

A.print_tree()

def is_symmetric(tree: BinaryTreeNode) -> bool:
    def check_symmetric(subtree_1, subtree_2):
        if not subtree_1 and not subtree_2:
            return True
        elif subtree_1 and subtree_2:
            return (subtree_1.data == subtree_2.data and check_symmetric(subtree_1.left, subtree_2.right) and check_symmetric(subtree_1.right, subtree_2.left))
        return False

    return not tree or check_symmetric(tree.left, tree.right)

print("Binary Tree is symmetric: " + str(is_symmetric(A)))
