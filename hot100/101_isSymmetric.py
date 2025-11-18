# 对称二叉树

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def isSymmetric(self, root: TreeNode) -> bool:
    '''层次遍历解法
    - 参考广搜做法
    '''
    if not root:
        return True
    
    node_list=[root.left,root.right]

    while node_list:
        level_size=len(node_list)

        if level_size%2!=0:  # 冗余
            return False
        
        for i in range(level_size//2):
            left_node = node_list[i]
            right_node = node_list[level_size-1-i]

            if not left_node and not right_node:
                continue


            if not left_node or not right_node or left_node.val != right_node.val:
                return False

        # 更新下一层节点
        next_level =[]
        for node in node_list:
            if node: # 节点不为空时添加，可以添加空
                next_level.append(node.left)
                next_level.append(node.right)
        node_list=next_level

    return True

def isSymmetric_1(self, root: TreeNode) -> bool:
    '''递归解法'''
    if not root:
        return True
    
    def isMirror(left:TreeNode, right:TreeNode)->bool:
        # 两个节点都为空，则对称
        if not left and not right:
            return True
        
        # 只有一个节点为空，则不对称
        if not left or not right:
            return False
        
        # 节点值相等，且左子树的左子树与右子树的右子树对称，
        # 左子树的右子树与右子树的左子树对称
        return (left.val == right.val and 
                isMirror(left.left, right.right) and 
                isMirror(left.right, right.left))  # 利用现有节点构造，对称子节点
    
    return isMirror(root.left,root.right)


def isSymmetric_2(self, root: TreeNode) -> bool:
    '''迭代解法，基于队列
    '''
    if not root:
        return True
    
    from collections import deque
    # 使用队列存储需要比较的节点对
    queue =deque([(root.left,root.right)]) # 存储为元组形式

    while queue:
        left,right= queue.popleft()

        if not left and not right:
            continue

        if not left or not right or left.val != right.val:
            return False
        
        # 📍 添加需要比较的节点对 （为树中的对称节点）
        queue.append((left.left,right.right))
        queue.append((left.right,right.left))
    
    return True