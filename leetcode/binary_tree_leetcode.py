class BinaryTreeNode:
    def __init__(self, data=None, left=None, right=None, parent=None, next=None):
        self.data = data
        self.left = left
        self.right = right
        self.parent = parent
        self.next = next


    def inorder(self, traversal):
        if self:
            if self.left:
                traversal = self.left.inorder(traversal)
            traversal += "-" + str(self.data) + "-"
            if self.right:
                traversal = self.right.inorder(traversal)
        return traversal


    def preorder(self, traversal):
        if self:
            traversal += "-" + str(self.data) + "-"
            if self.left:
                traversal = self.left.preorder(traversal)
            if self.right:
                traversal = self.right.preorder(traversal)
        return traversal


    def postorder(self, traversal):
        if self:
            if self.left:
                traversal = self.left.postorder(traversal)
            if self.right:
                traversal = self.right.postorder(traversal)
            traversal += "-" + str(self.data) + "-"
        return traversal


    def print_tree(self):
        print("Preorder: ".ljust(11) + self.preorder(""))
        print("Inorder: ".ljust(11) + self.inorder(""))
        print("Postorder: ".ljust(11) + self.postorder(""))


#     def depth(self):
#         if self.left and self.right:
#             return 1 + max(self.left.depth(), self.right.depth())
#         return 1
#
#
# A = BinaryTreeNode("A")
# B = BinaryTreeNode("B")
# C = BinaryTreeNode("C")
# D = BinaryTreeNode("D")
# E = BinaryTreeNode("E")
# F = BinaryTreeNode("F")
# G = BinaryTreeNode("G")
# H = BinaryTreeNode("H")
# I = BinaryTreeNode("I")
# J = BinaryTreeNode("J")
# K = BinaryTreeNode("K")
# L = BinaryTreeNode("L")
# M = BinaryTreeNode("M")
# N = BinaryTreeNode("N")
# O = BinaryTreeNode("O")
# X = BinaryTreeNode("X")
#
# A.left = B
# A.right = K
# B.left = C
# B.right = H
# C.left = D
# C.right = G
# D.left = E
# D.right = F
# H.left = I
# H.right = J
# K.left = L
# K.right = O
# L.left = M
# L.right = N
# N.right = X
#
# print(N.depth())
