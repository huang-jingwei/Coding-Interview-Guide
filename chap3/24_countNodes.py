# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# 基本思路：先进行层序遍历，然后再统计二叉树节点个数
class Solution:
    def countNodes(self, root: TreeNode) -> int:
        if root == None:
            return 0
        print(root)

        queue = []     # 层序遍历所需要的队列结构
        nodeData = []  # 层序遍历所需要的节点个数

        queue.append(root)
        while len(queue) > 0:
            node = queue.pop(0)
            if node != None:
                queue.append(node.left)
                queue.append(node.right)
            nodeData.append(node)
        # 去除层序遍历尾部的None节点
        while len(nodeData) > 0 and nodeData[-1] == None:
            nodeData.pop()
        nodeNum = len(nodeData)
        return nodeNum
