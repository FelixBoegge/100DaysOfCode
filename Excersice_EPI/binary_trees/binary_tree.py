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
            traversal += "-" + self.data + "-"
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
            traversal += "-" + self.data + "-"
        return traversal


    def print_tree(self, print_type):
        if print_type == "preorder":
            print("Preorder: ".ljust(11) + self.preorder(""))
        elif print_type == "inorder":
            print("Inorder: ".ljust(11) + self.inorder(""))
        elif print_type == "postorder":
            print("Postorder: ".ljust(11) + self.postorder(""))
        else:
            print("Invalid print type")
            return False

