class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self, root):
        self.root = Node(root)

    def print_tree(self, print_type):
        if print_type == "preorder":
            return "Preorder: ".ljust(11) + self.preorder(tree.root, "")
        elif print_type == "inorder":
            return "Inorder: ".ljust(11) + self.inorder(tree.root, "")
        elif print_type == "postorder":
            return "Postorder: ".ljust(11) + self.postorder(tree.root, "")
        else:
            print("Invalid print type")
            return False

    def preorder(self, start, traversal):
        if start:
            traversal += (str(start.value) + "--")
            traversal = self.preorder(start.left, traversal)
            traversal = self.preorder(start.right, traversal)
        return traversal

    def inorder(self, start, traversal):
        if start:
            traversal = self.inorder(start.left, traversal)
            traversal += (str(start.value) + "--")
            traversal = self.inorder(start.right, traversal)
        return traversal

    def postorder(self, start, traversal):
        if start:
            traversal = self.postorder(start.left, traversal)
            traversal = self.postorder(start.right, traversal)
            traversal += (str(start.value) + "--")
        return traversal

tree = BinaryTree(1)
tree.root.left = Node(2)
tree.root.right = Node(3)
tree.root.left.left = Node(4)
tree.root.left.right = Node(5)
tree.root.right.left = Node(6)
tree.root.right.right = Node(7)

print(tree.print_tree("preorder"))
print(tree.print_tree("inorder"))
print(tree.print_tree("postorder"))
