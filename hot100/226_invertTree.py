# 翻转二叉树
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def invertTree(root:TreeNode)->TreeNode:
    '''广搜
    逐个反转节点的子节点    
    '''
    if not root:
        return None

    node_list=[root]
    
    while node_list:
        leve_size=len(node_list)

        for _ in range(leve_size):
            node = node_list.pop()
            if node.left and node.right:
                node.left,node.right=node.right,node.left
                node_list.append(node.left)
                node_list.append(node.right)
            elif node.left:
                node.right=node.left
                node.left=None
                node_list.append(node.right)
            elif node.right:
                node.left=node.right
                node.right=None
                node_list.append(node.left)
    
    return root


def invertTree_DFS(root:TreeNode)->TreeNode:
    '''递归
    逐层反转节点
    '''
    if not root:
        return root
        
    # left = invertTree(root.left)
    # right = invertTree(root.right)
    # root.left, root.right = right, left

    # 等价写法
    root.left,root.right=root.right,root.left
    invertTree_DFS(root.left)
    invertTree_DFS(root.right)

    return root




if __name__ == "__main__":
    # 构建测试二叉树: [3,9,20,null,null,15,7]
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)

    # print(f"二叉树的最大深度（递归）: {maxDepth_Recursive(root)}")  # 应该输出 3