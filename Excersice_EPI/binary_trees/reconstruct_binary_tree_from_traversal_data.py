from binary_tree import BinaryTreeNode


def binary_tree_from_preorder_inorder(preorder, inorder) -> BinaryTreeNode:
    node_to_inorder_index = {data: i for i, data in enumerate(inorder)}

    def binary_tree_from_preorder_inorder_helper(preorder_start, preorder_end, inorder_start, inorder_end):
        if preorder_end <= preorder_start or inorder_end <= inorder_start:
            return None

        root_inorder_idx = node_to_inorder_index[preorder[preorder_start]]
        left_subtree_size = root_inorder_idx - inorder_start
        return BinaryTreeNode(
            preorder[preorder_start],\
            binary_tree_from_preorder_inorder_helper(
                preorder_start + 1, preorder_start + 1 + left_subtree_size, inorder_start, root_inorder_idx), \
            binary_tree_from_preorder_inorder_helper(
                preorder_start + 1 + left_subtree_size, preorder_end, root_inorder_idx + 1, inorder_end))

    return binary_tree_from_preorder_inorder_helper(preorder_start=0, preorder_end=len(preorder), inorder_start=0, inorder_end=len(inorder))

preoder = ['H', 'B', 'F', 'E', 'A', 'C', 'D', 'G', 'I']
inorder = ['F', 'B', 'A', 'E', 'H', 'C', 'D', 'I', 'G']

print(binary_tree_from_preorder_inorder(preoder, inorder).right.right.right.left.data)
