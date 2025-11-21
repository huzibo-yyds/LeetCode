# 路径总和 3
'''求该二叉树里节点值之和等于 targetSum 的路径的数目。
路径 不需要从根节点开始，也不需要在叶子节点结束，但是路径方向必须是向下的（只能从父节点到子节点）。
深度搜索
'''

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def pathSum(self, root: TreeNode, targetSum: int) -> int:
        ''' ⭐⭐
        1- 暴力DFS （从每个节点出发做深搜）        
        '''
        if root is None:
            return 0
        
        # 统计所有以node为起点，详细的路径，路径和为 remaining 的路径数量
        def count_path_from(node:TreeNode,remaining:int)->int:
            if node is None:
                return 0
            count = 0
            
            if node.val == remaining:
                count+=1
            
            # 递归遍历子树，注意目标值修改为 remaining-node.val
            count+=count_path_from(node.left,remaining-node.val)
            count+=count_path_from(node.right,remaining-node.val)

            return count

        # 对每个节点作为起点，调用 count_path_from 统计结果路径数，并遍历整个数累加结果
        def traverse(node:TreeNode)->int:
            if node is None:
                return 0
            path_from_current =count_path_from(node,targetSum)

            path_from_left = traverse(node.left)
            path_from_right = traverse(node.right)

            return path_from_current+path_from_left+path_from_right

        return traverse(root)

    
        


    def pathSum_2(self, root: TreeNode, targetSum: int) -> int:
        '''
        2- 前缀和 + 哈希表
            核心思路
            - 定义从当前节点到根节点的前缀和sum(curr)
            - 若存在某个在当前路径上的先前前缀和 prev，使得 sum(curr) - prev == targetSum，
                那么从 prev 的下一个节点到当前节点的这段路径和为 targetSum。
            - 因此需要一个哈希表 count，其中 count[s] 表示在当前递归路径上出现前缀和为 s 的次数
        '''
        pass