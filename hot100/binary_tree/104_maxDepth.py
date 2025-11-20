class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def maxDepth_Recursive(root:TreeNode) -> int:
    '''Recursive 递归实现
    深度优先搜索
    '''
    if not root:
        return 0
    
    left_depth = maxDepth_Recursive(root.left)
    right_depth = maxDepth_Recursive(root.right)

    return max(left_depth,right_depth)+1

def maxDepth_Iterative(root:TreeNode) -> int:
    '''广度优先搜索
    '''
    if not root:
        return 0
    
    # deque，双端队列，允许在队列两端高效插入和删除
    from collections import deque
    queue=deque([root])
    depth = 0

    while queue:
        level_size = len(queue)

        # 逐层处理，向下遍历
        for _ in range(level_size):
            node=queue.popleft()

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
    
            depth+=1
    
    return depth


if __name__ == "__main__":
    # 构建测试二叉树: [3,9,20,null,null,15,7]
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)

    print(f"二叉树的最大深度（递归）: {maxDepth_Recursive(root)}")  # 应该输出 3
