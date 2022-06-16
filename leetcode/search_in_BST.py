from binary_tree_leetcode import BinaryTreeNode

a = BinaryTreeNode(4)
b = BinaryTreeNode(2)
c = BinaryTreeNode(7)
d = BinaryTreeNode(1)
e = BinaryTreeNode(3)
a.left = b
a.right = c
b.left = d
b.right = e

def searchBST(root: [BinaryTreeNode], val: int) -> [BinaryTreeNode]:
    if root.data == val:
        return root
    elif root.data > val:
        root = searchBST(root.left, val)
    else:
        root = searchBST(root.right, val)
    return root

root = [a,b,c,d,e]
val = 4

print(searchBST(a, val).print_tree())
