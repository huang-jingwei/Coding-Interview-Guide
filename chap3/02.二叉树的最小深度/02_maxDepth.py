# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if root==None:
            return 0
        leftHeight=self.maxDepth(root.left)
        rightHeight=self.maxDepth(root.right)
        return max(leftHeight,rightHeight)+1