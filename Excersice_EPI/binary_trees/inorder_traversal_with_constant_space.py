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
B.parent = A
C.parent = B
D.parent = C
E.parent = D
F.parent = D
G.parent = C
H.parent = B
I.parent = H
J.parent = H
K.parent = A
L.parent = K
M.parent = L
N.parent = L
O.parent = K

A.print_tree()

def inorder(tree: BinaryTreeNode):
    prev, result = None, []
    while tree:
        if prev is tree.parent:
            if tree.left:
                next = tree.left
            else:
                result.append("-" + tree.data + "-")
                next = tree.right or tree.parent
        elif tree.left is prev:
            result.append("-" + tree.data + "-")
            next = tree.right or tree.parent
        else:
            next = tree.parent

        prev, tree = tree, next
    return result


print("\nInorder: ".ljust(12) + ''.join(inorder(A)))
