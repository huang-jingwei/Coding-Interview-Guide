# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSubStructure(self, A: TreeNode, B: TreeNode) -> bool:
        # 一个树A包含另一个树B 则
        # 1、 要么B树被包含A树
        # 2、 要么B树被包含A左树的子树
        # 3、 要么B树被包含A右树的子树

        # 按照题目约定空树不是任意一个树的子结构
        if B == None:
            return False

        # 经过上面一步的筛除，此刻B必定不为空
        if A == None:
            return False

        # 情况1： 要么B树被包含A树
        if self.isContain(A, B) == True:
            return True
        # 情况2： 要么B树被包含A左树的子树
        # 情况3： 要么B树被包含A右树的子树
        return self.isSubStructure(A.left, B) or self.isSubStructure(A.right, B)

    # 函数功能：判断root1头节点所生产的二叉树是否包含root2头节点所生成的二叉树结构
    def isContain(self, root1, root2):
        # 按照题目约定空树不是任意一个树的子结构
        if root2 == None:
            return True

        # 经过上面一步的筛除，此刻root2必定不为空
        if root1 == None or root1.val != root2.val:
            return False

        return self.isContain(root1.left, root2.left) and self.isContain(root1.right, root2.right)
