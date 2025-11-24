# 二叉树的最近公共祖先 （深度尽量大，尽可能低的祖先）

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root:
            return None
        p_prefix=[]
        q_prefix=[]

        # 定义一个查找路径并回溯的辅助函数
        def dfs(node:TreeNode,target:TreeNode,pre_fix:list):
            '''
            与简单的遍历不同，需要回溯，从路径列表中删除非祖先节点
            '''
            if not node:
                return False
            pre_fix.append(node)

            if node == target:
                return True
            if dfs(node.left,target,pre_fix) or dfs(node.right,target,pre_fix):
                return True
            
            pre_fix.pop()
            return False
        
        # 获取从root到节点的路径
        dfs(root,p,p_prefix)
        dfs(root,q,q_prefix)

        # 从头往后遍历两条路径，找到最后一个公共点
        result = None
        for i in range(min(len(p_prefix),len(q_prefix))):
            if p_prefix[i]==q_prefix[i]:
                result=p_prefix[i]
            else:
                break

        return result
