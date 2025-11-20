# 二叉树层次遍历
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# 返回的是节点值，而非节点列表
class Solution:
    def levelOrder(self, root: TreeNode) -> list[list[int]]:
        ''' 广度优先搜索
        使用duque队列存储当前层次节点，逐层逐节点遍历更新
        
        '''
        if not root:
            return []
        
        from collections import deque
        node_list = deque([root]) # 当前层次节点
        # all_node_list = [[root]] # 全部节点层次化结果
        res = []
        while node_list:
            level_size = len(node_list)
            level_val = []
            for _ in range(level_size):
                node = node_list.popleft()
                level_val.append(node.val)

                # 更新节点
                if node.left:
                    node_list.append(node.left)
                if node.right:
                    node_list.append(node.right)

            res.append(level_val)
            # all_node_list.append(node_list)

        return res
