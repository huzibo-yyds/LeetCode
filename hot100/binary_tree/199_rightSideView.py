# 二叉树的右视图
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def rightSideView(self, root: TreeNode) -> list[int]:
        ''' 广搜，层次遍历
        将每层最后一个节点值记录下来
        '''

        if not root:
            return []

        result=[]

        from collections import deque
        node_list =deque([root])
        # deque 初始化需要注意

        while node_list:
            level_size = len(node_list)
            result.append(node_list[-1].val)
            for _ in range(level_size):
                node=node_list.popleft()
                if node.left:
                    node_list.append(node.left)
                if node.right:
                    node_list.append(node.right)

        return result
