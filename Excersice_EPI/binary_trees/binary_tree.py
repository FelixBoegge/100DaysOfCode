class BinaryTreeNode:
    def __init__(self, data=None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


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
