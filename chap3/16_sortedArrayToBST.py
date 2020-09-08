# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        if len(nums) == 0:
            return None

        head = self.buildTree(nums)
        return head

    def buildTree(self, array):
        arrayLength = len(array)
        if arrayLength == 0:
            return None
        mid = (arrayLength) // 2
        head = TreeNode(array[mid])
        head.left = self.buildTree(array[:mid])
        head.right = self.buildTree(array[mid + 1:])
        return head