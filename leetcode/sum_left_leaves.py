from binary_tree_leetcode import BinaryTreeNode


def sumOfLeftLeaves(root: [BinaryTreeNode]) -> int:
    def is_leave(node):
        return True if not node.left and not node.right else False

    if not root:
        return 0
    nodes = [[root, "right"]]
    sum_left_leaves = 0

    while nodes:
        cur_node, side = nodes.pop()
        if cur_node.left:
            nodes.append([cur_node.left, "left"])
        if cur_node.right:
            nodes.append([cur_node.right, "right"])
        if side == "left" and is_leave(cur_node):
            sum_left_leaves += cur_node.data

    return sum_left_leaves