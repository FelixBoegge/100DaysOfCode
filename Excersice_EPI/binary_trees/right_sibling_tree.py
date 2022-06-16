from binary_tree import BinaryTreeNode

A = BinaryTreeNode("A")
B = BinaryTreeNode("B")
C = BinaryTreeNode("C")
D = BinaryTreeNode("D")
G = BinaryTreeNode("G")
H = BinaryTreeNode("H")
I = BinaryTreeNode("I")
J = BinaryTreeNode("J")
K = BinaryTreeNode("K")
L = BinaryTreeNode("L")
M = BinaryTreeNode("M")
N = BinaryTreeNode("N")
O = BinaryTreeNode("O")
P = BinaryTreeNode("P")
Q = BinaryTreeNode("Q")


A.left = B
A.right = K
B.left = C
B.right = H
C.left = D
C.right = G
H.left = I
H.right = J
K.left = L
K.right = O
L.left = M
L.right = N
O.left = P
O.right = Q


def construct_right_sibling(tree: BinaryTreeNode) -> None:
    def populate_children_next_field(start_node):
        while start_node and start_node.left:
            start_node.left.next = start_node.right
            start_node.right.next = start_node.next and start_node.next.left
            start_node = start_node.next

    while tree and tree.left:
        populate_children_next_field(tree)
        tree = tree.left

construct_right_sibling(A)

print(D.next.data)