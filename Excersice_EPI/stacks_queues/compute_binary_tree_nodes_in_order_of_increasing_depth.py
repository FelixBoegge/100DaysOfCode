def binary_tree_depth_order(tree):
    result: []
    if not tree:
        return result

    cur_depth_nodes = [tree]
    while cur_depth_nodes:
        result.append([cur.data for cur in cur_depth_nodes])
        cur_depth_nodes = [child for cur in cur_depth_nodes for child in (cur.left, cur.right) if child]
    return result

