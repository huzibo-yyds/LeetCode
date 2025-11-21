# 二叉搜索树中第 K 小的元素

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        '''
        核心思路：二叉树中序遍历
        利用二叉搜索树 BST 的性质，经过中序遍历得到一个严格递增的有序序列
        从序列中获得第 k 个元素即可
        '''

        val=[]
        flag=k

        stack=[]
        current = root
        while current or stack:
            while current:
                stack.append(current)
                current=current.left
            
            current=stack.pop()
            val.append(current.val)
            flag-=1
            if flag==0:
                return val.pop()

            current=current.right

