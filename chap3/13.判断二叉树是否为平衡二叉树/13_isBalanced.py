# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        if root == None:
            return True
        leftHeight = self.height(root.left)
        rightHeight = self.height(root.right)
        return abs(leftHeight - rightHeight) <= 1 and self.isBalanced(root.left) and self.isBalanced(root.right)

    # 计算一个节点能构成的二叉树的高度
    def height(self, root):
        if root == None:
            return 0
        leftHeight = self.height(root.left)
        rightHeight = self.height(root.right)
        return max(leftHeight, rightHeight) + 1