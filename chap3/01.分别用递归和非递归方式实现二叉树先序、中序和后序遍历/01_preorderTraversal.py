# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# 前序遍历打印顺序：中左右
class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        if root == None:
            return []
        prePrintNode = []  # 前序遍历返回的节点数值
        stack = []         # 辅助栈结构
        stack.append(root)
        while len(stack) > 0:
            node = stack.pop()
            prePrintNode.append(node.val)
            if node.right != None:
                stack.append(node.right)
            if node.left != None:
                stack.append(node.left)
        return prePrintNode