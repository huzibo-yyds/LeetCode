# 验证二叉搜索树
'''
有效 二叉搜索树定义如下：

节点的左子树只包含 严格小于 当前节点的数。
节点的右子树只包含 严格大于 当前节点的数。
所有左子树和右子树自身必须也是二叉搜索树
'''

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        '''
        中序遍历，判断是否从大到小
        '''

        prev=float('-inf') # 记录上一个访问到的节点值，初始化为-♾️  需要确保严格从小到大

        def inorder(node):
            nonlocal prev # 声明此处pre变量并非局部变量 ❗️

            # 空节点返回 True，不影响有效性
            if not node:
                return True
            
            # 递归遍历左子树，若已经违反 BST，则向上传 False
            if not inorder(node.left):
                return False

            # 📍 真正比较部分，需要确保前一个元素值严格小于当前元素
            if node.val <= prev:
                return False
            prev=node.val
            
            # 继续遍历右子树
            return inorder(node.right)
        
        return inorder(root)
    
    def isValidBST_2(self, root: TreeNode) -> bool:
        '''
        迭代实现中序遍历 更容易理解
        '''

        stack=[]
        inorder = float('-inf')

        while stack or root:
            # 遍历左子树
            while root:
                stack.append(root)
                root=root.left
            root= stack.pop()

            if root.val<= inorder:
                return False
            
            inorder = root.val
            root=root.right
        
        return True