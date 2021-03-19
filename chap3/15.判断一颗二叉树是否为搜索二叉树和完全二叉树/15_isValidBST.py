# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        if root == None:
            return True
        # 搜索二叉树的中序遍历是升序序列
        nodeData = self.inOrderPrint(root)
        for index in range(len(nodeData) - 1):
            if nodeData[index] >= nodeData[index + 1]:
                return False
        return True

    # 二叉树的中序遍历
    def inOrderPrint(self, root):
        if root == None:
            return []
        nodeData = []
        leftNode = self.inOrderPrint(root.left)
        if len(leftNode) > 0:
            for nodeVal in leftNode:
                nodeData.append(nodeVal)
        nodeData.append(root.val)
        rightNode = self.inOrderPrint(root.right)
        if len(rightNode) > 0:
            for nodeVal in rightNode:
                nodeData.append(nodeVal)
        return nodeData