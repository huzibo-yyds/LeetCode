# 二叉树展开为列表
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        node_list=[]

        def preorder(root):
            '''前序遍历'''
            if not root:
                return
            node_list.append(root)
            preorder(root.left)
            preorder(root.right)

        preorder(root)
        for i in range(len(node_list)-1):
            node=node_list[i]
            node.left=None
            node.right=node_list[i+1]
