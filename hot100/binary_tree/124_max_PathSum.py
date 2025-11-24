# 二叉树走最大路径和
# 一条节点序列，序列中每对相邻节点之间都存在一条边。
# 该路径 至少包含一个 节点，且不一定经过根节点。

'''
1、理解路径 路径方向是“向下”的，但可以在某个节点“拐弯” 
 左子树 - 拐弯 - 右子树

两类路径
 1- 不拐弯，从node出发单向延伸到左、右子树
 2- 拐弯，以node为顶，分别连接左右子树中指最大的单向路径

2、如何递归
 1- 为父节点服务，计算并返回一个值，这个值代表从当前节点 node 出发，只能往下走（不拐弯） 的最大路径和
 2- 更新全局结果，在当前node，计算一个可能拐弯的最大值

3、后序遍历比较合适
 1- 计算左子树最大值
 2- 计算右子树最大值
 3- 更新当前结果

'''


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        ''' 动态规划 | 深搜
        
        '''

        if not root:
            return 0
        
        max_sum=float('-inf')

        def maxGain(node:TreeNode):
            nonlocal max_sum
            if not node:
                return 0
            
            leftGain=max(maxGain(node.left),0)
            rightGain=max(maxGain(node.right),0)
            
            crruent_max=leftGain+node.val+rightGain

            max_sum=max(crruent_max,max_sum)

            return node.val + max(leftGain,rightGain) # 返回节点最大贡献


        maxGain(root)
        return max_sum
