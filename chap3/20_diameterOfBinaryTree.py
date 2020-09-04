# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:

    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        if root == None:
            return 0
        leftHeight = self.height(root.left)
        rightHeight = self.height(root.right)
        curDistance = max(leftHeight, rightHeight, leftHeight + rightHeight)  # 当前节点能构成的最大直径

        return max(curDistance, self.diameterOfBinaryTree(root.left), self.diameterOfBinaryTree(root.right))

    # 计算一个节点作为头结点时所能构成的二叉树的高度
    def height(self, root):
        if root == None:
            return 0
        leftHeight = self.height(root.left)
        rightHeight = self.height(root.right)
        return max(leftHeight, rightHeight) + 1