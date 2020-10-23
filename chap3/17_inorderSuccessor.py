# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def inorderSuccessor(self, root: TreeNode, p: TreeNode) -> TreeNode:
        if root == None:
            return None
        postPrintArray = self.postPrint(root)  # 二叉树的中序遍历数组
        for index in range(len(postPrintArray)):
            if p == postPrintArray[index]:
                if index + 1 < len(postPrintArray):
                    postItem = postPrintArray[index + 1]
                    return postItem
                else:
                    return None
        return None

    # 二叉树的中序遍历
    def postPrint(self, root):
        if root == None:
            return []
        array = []
        leftArray = self.postPrint(root.left)
        if len(leftArray) > 0:
            for node in leftArray:
                array.append(node)
        array.append(root)
        rightArray = self.postPrint(root.right)
        if len(rightArray) > 0:
            for node in rightArray:
                array.append(node)
        return array