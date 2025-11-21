# 将有序数组转换为二叉搜索数
# 平衡二叉树 是指该树所有节点的左右子树的高度相差不超过 1。

'''
【题目理解】
高度平衡的定义：任意节点的左右子树高度差不超过 1。
BST 性质：任意节点，左子树所有值 < 该节点值 < 右子树所有值。
（由于数组有序，利用中间元素作为根，左右数量尽可能接近，达到平衡）

【分治思想】 helper 函数
终止条件：left > right，表示子数组为空，返回 None。
选根：mid = (left + right) // 2
构建节点：root = TreeNode(nums[mid])
递归构左子树：helper(left, mid - 1)
递归构右子树：helper(mid + 1, right)
返回 root
整体调用 helper(0, len(nums) - 1)。

'''

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def sortedArrayToBST(self, nums: list[int]) -> TreeNode:

        def helper(left,right):
            # 终止条件
            if left > right:
                return None
            # 选择中间元素作为根，确保平衡
            mid =(left+right)//2
            
            # 当前根节点
            root = TreeNode(nums[mid])

            # 构造左右子树
            root.left=helper(left,mid-1)
            root.right=helper(mid+1,right)

            return root
        
        return helper(0,len(nums)-1) # helper 闭区间处理