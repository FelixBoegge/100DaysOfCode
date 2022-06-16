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



def create_list_of_leaves(tree: BinaryTreeNode) ->[BinaryTreeNode]:
    if not tree:
        return []
    if not tree.left and not tree.right:
        return [tree]
    return create_list_of_leaves(tree.left) + create_list_of_leaves(tree.right)

print(list(x.data for x in create_list_of_leaves(A)))
