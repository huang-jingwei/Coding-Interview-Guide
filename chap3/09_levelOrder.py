# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if root == None:        # 二叉树头结点为空时，返回空列表
            return []

        nodeData = []           # 存放每一层节点的信息
        queue = []              # 层序遍历的队列结构
        queue.append(root)

        while queue:
            nextFloorNode = []  # 初始化列表，存放下一层节点信息
            nodeVal = []        # 初始化列表，存放当前层节点的数值

            for node in queue:  # 遍历当前层节点，依次压入左右儿子节点
                nodeVal.append(node.val)
                if node.left != None:
                    nextFloorNode.append(node.left)
                if node.right != None:
                    nextFloorNode.append(node.right)

            queue = nextFloorNode # 移动到下一层树节点
            nodeData.append(nodeVal)
        return nodeData