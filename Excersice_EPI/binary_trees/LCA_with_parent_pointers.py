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

def lca(node1: BinaryTreeNode, node2: BinaryTreeNode) ->BinaryTreeNode:
    def get_depth(node):
        depth = 0
        while node.parent:
            depth += 1
            node = node.parent
        return depth

    depth1, depth2 = get_depth(node1), get_depth(node2)
    if depth2 > depth1:
        node1, node2 = node2, node1

    depth_diff = abs(depth1 - depth2)
    while depth_diff:
        node1 = node1.parent
        depth_diff -= 1

    while node1 is not node2:
        node1, node2 = node1.parent, node2.parent

    return node1

n1 = M
n2 = N

print(f"The LCA of {n1.data} and {n2.data} is: " + lca(n1, n2).data)
