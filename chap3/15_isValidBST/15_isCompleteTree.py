# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# 根据完全二叉树的定义
# 情形1、完全二叉树的层序遍历中不能出现None节点
# 情形2、若一个节点只存在右儿子节点，则必然存在左儿子节点
# 情形3、若一个节点只存在左儿子节点，那么该节点的左儿子节点必须为最后一个节点
class Solution:
    def isCompleteTree(self, root: TreeNode) -> bool:
        if root == None:  # 输入二叉树为空二叉树
            return True
        elif root.left == None and root.right == None:  # 输入二叉树只有头节点
            return True

        queue = []  # 层序遍历中的辅助队列结构
        nodeData = []  # 层序遍历中的节点
        queue.append(root)
        while len(queue) > 0:
            node = queue.pop(0)
            if node != None:
                queue.append(node.left)
                queue.append(node.right)
            nodeData.append(node)

        # 去除层序遍历后面多余的None节点
        while len(nodeData) > 0 and nodeData[-1] == None:
            nodeData.pop()

        firstBreakNode = None  # 用来记录第一个只存在左儿子节点的节点
        for index in range(len(nodeData)):
            # 情形1、完全二叉树的层序遍历中不能出现None节点
            if nodeData[index] == None:
                return False
            # 情形2、若一个节点只存在右儿子节点，则必然存在左儿子节点
            elif nodeData[index].left == None and nodeData[index].right != None:
                return False
            # 情形3、若一个节点只存在左儿子节点，那么该节点的左儿子节点必须为最后一个节点
            # 找出第一个只存在左儿子节点的节点
            elif nodeData[index] != None and nodeData[index].left != None and nodeData[index].right == None:
                firstBreakNode = nodeData[index].left
                break
        if firstBreakNode != None:  # 存在节点node只存在左儿子节点
            # 找出node节点的左儿子节点的下标
            for i in range(index, len(nodeData)):
                if nodeData[i] == firstBreakNode:
                    firstBreakIndex = i
                    break
            # 在该节点的左儿子节点必须为最后一个节点
            if firstBreakIndex != len(nodeData) - 1:
                return False
        return True