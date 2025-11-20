# 二叉树直径
'''
二叉树的 直径 是指树中任意两个节点之间最长路径的 长度 。这条路径可能经过也可能不经过根节点 root 。
两节点之间路径的 长度 由它们之间边数表示。
'''

class TreeNode:
    def __init__(self,val=0,left=None,right=None):
        self.val=val
        self.left = left
        self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        '''
        对每个节点，计算其左右子树的深度，节点处可能的最长路径为左深度 + 右深度（边数）
        深度优先搜索
        '''
        ans=[0]

        # 返回以 node 为根的子树的深度（以节点数计，叶子为 1）
        def depth(node:TreeNode)->int:
            # 解决方法二
            # nonlocal ans  # 声明ans不是局部变量
            if not node: # 1- 基本情况
                return 0
            
            L = depth(node.left) # 2- 递归计算左右深度
            R = depth(node.right)

            if L+R > ans[0]: # 3-更新直径
                ans[0]=L+R
            
            return max(L,R) + 1 # 返回以node节点为根的子树深度
        
        depth(root)
        return ans[0]

if __name__ == "__main__":
    # 示例：二叉树 [1,2,3,4,5]，直径为 3（路径 4-2-1-3 或 5-2-1-3）
    n1 = TreeNode(1)
    n2 = TreeNode(2)
    n3 = TreeNode(3)
    n4 = TreeNode(4)
    n5 = TreeNode(5)
    n1.left, n1.right = n2, n3
    n2.left, n2.right = n4, n5

    print(Solution().diameterOfBinaryTree(n1))  # 输出 3