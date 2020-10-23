# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if root == None:
            return 0

        level = 0   # 记录二叉树层序遍历的层数

        queue = []  # 二叉树层序遍历的辅助队列结构
        queue.append(root)

        while len(queue) > 0:
            nextNode = []  # 二叉树下一层节点
            level += 1
            for node in queue:
                if node.left != None:
                    nextNode.append(node.left)
                if node.right != None:
                    nextNode.append(node.right)
                if node.left == None and node.right == None:
                    return level
            queue = nextNode
        return level