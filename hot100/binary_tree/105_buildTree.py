# 从前序与中序遍历序列构造二叉树

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def buildTree(self, preorder: list[int], inorder: list[int]) -> TreeNode:
        '''
        preorder, 是二叉树的先序遍历，根-左-右
            [根节点, [左子树的前序遍历], [右子树的前序遍历]]
        inorder，是二叉树的中序遍历，左-根-右
            [[左子树的中序遍历], 根节点, [右子树的中序遍历]]

        递归分治
        1、找到根节点
        2、分割左右子树
        3、获得子树的遍历顺序 pre/ in
        4、递归构造
        5、当传入的队列为空时，返回None
        '''

        inorder_map ={}
        for i,val in enumerate(inorder):
            inorder_map[val]=i # 值为键、索引i为值
        # 等价写法
        # inorder_map = {val: i for i, val in enumerate(inorder)}

        def build(pre_left,pre_right, # 前序闭区间
                  in_left,in_right):  # 中序比区间
            # 终止条件
            if pre_left>pre_right:
                return None
            
            # 核心操作，创建节点
            root_val = preorder[pre_left]
            root=TreeNode(root_val)
            in_root_idx = inorder_map[root_val]

            left_subtree_size= in_root_idx - in_left

            # 递归构建左子树
            root.left= build(pre_left+1,pre_left+left_subtree_size,
                             in_left,in_root_idx-1)
            
            # 递归构建右子树
            root.right=build(pre_left+left_subtree_size+1,pre_right,
                             in_root_idx+1,in_right)
            
            return root
        
        n = len(preorder)
        return build(0,n-1,0,n-1)

        