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
            将求“ 两点间路径和问题 ” -> “求两个前缀和的查的问题”
            问题定义：prefix(C) - prefix(P) = targetSum （C为当前节点，P为祖先节点）
            当我们遍历到节点 C 时，在从根到 C 的路径上，我们只需要回头找一找，之前出现过多少个前缀和恰好等于 prefix(C) - targetSum

            - 定义从当前节点到根节点的前缀和sum(curr)
            - 若存在某个在当前路径上的先前前缀和 prev，使得 sum(curr) - prev == targetSum，
                那么从 prev 的下一个节点到当前节点的这段路径和为 targetSum。
            - 因此需要一个哈希表 count，其中 count[s] 表示在当前递归路径上出现前缀和为 s 的次数

            ‘哈希表’ 在python中为dict
            - 用于高效完成回头找，前缀节点

        '''
        if root is None:
            return 0
        
        prefix_counts = {0:1}
        ans = 0 # 结果计数

        def dfs(node:TreeNode, curr_sum:int):
            nonlocal ans
            if node is None:
                return
            
            curr_sum+=node.val

            # 📍关键计算 prefix(P)  = prefix(C) - targetSum
            ans+= prefix_counts.get(curr_sum-targetSum,0) # Return the value for key if key is in the dictionary, else default.

            # 将当前前缀和加入哈希表
            prefix_counts[curr_sum] = prefix_counts.get(curr_sum,0) + 1

            dfs(node.left,curr_sum)
            dfs(node.right,curr_sum)

            # 回溯：离开当前节点时撤销当前前缀和的计数，确保哈希表只反映当前路径
            prefix_counts[curr_sum]-=1

            #
            if prefix_counts[curr_sum] == 0:
                del prefix_counts[curr_sum]
        
        dfs(root,0)
        return ans
        