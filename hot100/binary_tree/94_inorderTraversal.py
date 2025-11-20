# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    '''中序遍历 (Inorder)
    左子树 - 根 - 右子树 (LDR)
    '''
    def inorderTraversal_Recursive(self, root: TreeNode) -> list[int]:
        '''递归实现'''
        result=[]

        def inorder(node):
            if not node:
                return
            
            inorder(node.left)
            result.append(node.val)
            inorder(node.right)

        inorder(root)
        return result
    
    def inorderTraversal_Iterative(self,root:TreeNode) -> list[int]:
        '''迭代实现'''
        result = []
        stack = [] # 迭代，显式将栈模拟出来
        current = root

        while current or stack:
            while current:
                stack.append(current) # 节点入栈
                current=current.left  # 左

            current = stack.pop
            result.append(current.val) # '根'

            current=current.right # 右
        
        return result