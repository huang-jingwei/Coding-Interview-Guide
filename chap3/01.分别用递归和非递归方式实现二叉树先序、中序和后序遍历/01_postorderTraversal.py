# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# 后序遍历的打印顺序：左右中
class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        if root == None:
            return []
        postPrintData = []  # 后序遍历输出的节点
        stack = []          # 辅助数据栈
        nodeData = []
        stack.append(root)

        while len(stack) > 0:
            node = stack.pop()
            nodeData.append(node.val)
            if node.left != None:
                stack.append(node.left)
            if node.right != None:
                stack.append(node.right)

        while len(nodeData) > 0:
            item = nodeData.pop()
            postPrintData.append(item)
        return postPrintData